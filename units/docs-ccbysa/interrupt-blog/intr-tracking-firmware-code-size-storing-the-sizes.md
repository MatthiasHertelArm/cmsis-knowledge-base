---
id: "intr-tracking-firmware-code-size-storing-the-sizes"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size / Storing the Sizes"
summary: "We now want to store our sizes in our newly minted PostgreSQL database. Your database provider or devops engineer will likely give you a URL string that looks like:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#storing-the-sizes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How to Track Code Size_

We now want to store our sizes in our newly minted PostgreSQL database. Your
database provider or devops engineer will likely give you a URL string that
looks like:

```
postgres://<username>:<password>@<server>:<port>/<database_name>
```

We can use this in a Python script to insert and fetch rows from the database
using the `psycopg2` library. Unfortunately, going into the details, nuances,
and pitfalls about how one interacts with and manages a database is out of the
scope of this post. I have listed SQL operations below that a developer could
use, and I have also written up a
[working example](https://github.com/memfault/interrupt/tree/master/example/code-size-deltas/codesizes.py)
that you can use with a few modifications.

For now, let's quickly go through using `pyscopg2` in a Python script.

First, we need to make a connection to the PostgreSQL database from within our
Python script.

```python
DATABASE_URL = os.environ.get("DATABASE_URL", 'postgresql://localhost:5432/codesizes')
url = urlparse(DATABASE_URL)
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
```

To initialize the database with our table and all the necessary columns, we
first have to issue a `CREATE TABLE` command.

```python
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE "codesizes" (
        "created_at" timestamp NOT NULL DEFAULT NOW(),
        "revision" varchar NOT NULL,
        "build" varchar NOT NULL,
        "parent_revision" varchar NOT NULL,
        "text" int4 NOT NULL,
        "data" int4 NOT NULL,
        "bss" int4 NOT NULL,
        "message" varchar NOT NULL DEFAULT ''::character varying,
        PRIMARY KEY ("revision","build")
    )
    """
)
conn.commit()
```

Now we have a database and table that is ready to accept code sizes!

To push one, we'll use the `INSERT INTO` operation.

```python
codesize = CodesizeData(
    # class with all code size info
)
cursor.execute("""
    INSERT INTO codesizes
        (revision, build, parent_revision, text, data, bss, message)
    VALUES ('{}', '{}', '{}', {}, {}, {}, '{}')
    """.format(codesize.revision, codesize.build,
               codesize.parent_revision,
               codesize.text, codesize.data,
               codesize.bss, codesize.message
    )
)
conn.commit()
```

Finally, to fetch a value from the database, a `SELECT` operation can be used.

```python
cursor.execute("""
    SELECT
      revision, build, parent_revision,
      text, data, bss, message
    FROM codesizes
    WHERE build = '{}'
      AND revision = '{}'
    """.format(build, revision)
)
record = cursor.fetchone()
revision, build, parent_revision, text, data, bss, message = record
return CodesizeData(
    # Fill in class data
)
```

All of these code snippets shown above can be found in the Interrupt repo in a
[mostly working example](https://github.com/memfault/interrupt/tree/master/example/code-size-deltas/codesizes.py).

Wrapping these SQL operations with Python and
[Click](https://click.palletsprojects.com/en/7.x/) makes the operation of
"stamping" and uploading a code size something like the following:

```python
@cli.command()
@click.argument("binary")
@click.option("--build", default="default")
@click.option("--revision", default="HEAD")
def stamp(binary, build, revision):
    """
    Calculates the size of the BINARY (.elf) provided and
    stamps the current git revision with the code size for
    the given BUILD.
    """
    text, data, bss = _calculate_codesize(binary)
    # git rev-parse <revision>^1
    parent_revision = _get_parent_revision(revision)
    # git log -1 --pretty=%s <revision>
    message = _get_git_log_line(revision)
    # Insert code size into database
    codesize = CodesizeData([...])
    _upload_codesize(codesize)
```

If you are using the examples from above, you'd place something like the
following in your CI system after the firmware has been built.

```
export DATABASE_URL = # set this in a global CI config
$ python ~/codesizes.py stamp build/zephyr/zephyr.elf \
    --build lwm2m_client
```
