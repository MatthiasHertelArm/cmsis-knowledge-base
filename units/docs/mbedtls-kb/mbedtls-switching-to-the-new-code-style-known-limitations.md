---
id: "mbedtls-switching-to-the-new-code-style-known-limitations"
type: "concept"
domain: "security"
title: "Switching to the new code style: Known limitations"
summary: "The automatic rewriting script can fail if an intermediate commit contains syntactically incorrect C code, for example unbalanced braces. If the script fails in an uncrustify command, this is the most likely reason."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/rewrite-branch-for-coding-style.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/rewrite-branch-for-coding-style.md#known-limitations"
license: "Apache-2.0"
mode: "V"
---

### Syntactically invalid commits

The automatic rewriting script can fail if an intermediate commit contains syntactically incorrect C code, for example unbalanced braces. If the script fails in an `uncrustify` command, this is the most likely reason.

Workaround: first do a manual rebase where you fix the syntax of the problematic commit.

Here is an example transcript with the end of the `--verbose` output showing this problem:
```
...
Applying efef9ffbba73433323137d22d7c675e9ceb0291c onto cb0ca794a4a7bea9db82659b6d4ae8b3e43ef9ee
efef9ffbba73433323137d22d7c675e9ceb0291c has been cherry-picked as c8a5ca2a1dbd3d4a0bf08b0216d8224bca8993fe
efef9ffbba73433323137d22d7c675e9ceb0291c has been amended to 8ae5bf5f1b7441d27d4b0c616d44f7ecba0691a7
Will restyle: library/x509_crt.c
Pass #0 of uncrustify
do_source_file(1507): Parsing: library/x509_crt.c as language C
parse_cleanup(528): pc->orig_line is 845, orig_col is 1, Text() is '}', type is BRACE_CLOSE
process_return(2180): temp->level is ZERO, cannot be decremented, at line 844, column 11
Traceback (most recent call last):
  File "../../bin/mbedtls-rewrite-branch-style", line 591, in <module>
    sys.exit(main())
  File "../../bin/mbedtls-rewrite-branch-style", line 575, in main
    branch_rewriter.rewrite(args.branch, update_existing_branch)
  File "../../bin/mbedtls-rewrite-branch-style", line 280, in rewrite
    self.do_rewrite(branch)
  File "../../bin/mbedtls-rewrite-branch-style", line 528, in do_rewrite
    self.restyle_commit_onto_current(new_commit)
  File "../../bin/mbedtls-rewrite-branch-style", line 496, in restyle_commit_onto_current
    self.restyle_files(files_to_restyle)
  File "../../bin/mbedtls-rewrite-branch-style", line 466, in restyle_files
    subprocess.check_call([self.UNCRUSTIFY_EXE,
  File "/usr/lib/python3.8/subprocess.py", line 364, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['uncrustify', '-c', '.uncrustify.cfg', '--no-backup', 'library/x509_crt.c']' returned non-zero exit status 70.
```
Look for the last “Applying ...” line in the transcript. Run `git show -s efef9ffbba73433323137d22d7c675e9ceb0291c` to list the commit date and commit message. Find this commit in your working branch (use `git log`); it will have a different commit ID because the commit ID in the transcript is after a rebase. In this example, the original commit with the same commit message was `93e4f76a3e9ca2d2448525657b3e0f7b3c6ed863`. To rewrite this commit, do an interactive rebase and ask to `93e4f76a3e9ca2d2448525657b3e0f7b3c6ed863`, keeping other commits intact. The last line of the transcript shows which file has the syntax error, and the previous messages give a hint as to where the error is. In the example above, the file is `library/x509_crt.c` and the error was detected at line 844. The actual problem turns out to be a missing `*/` a few lines above.

### Branches with merges

The rewrite script was written for simple cases of branches that fork from an official branch of Mbed TLS, and do not contain additional merges. If a branch contains merges, the script will fail.

Workaround: manually rebase on top of the last commit before the style change. If there are no merges left in your branch, you can use the script to do the rest of the work. Otherwise you'll need to do a manual merge instead of rewriting your branch.
