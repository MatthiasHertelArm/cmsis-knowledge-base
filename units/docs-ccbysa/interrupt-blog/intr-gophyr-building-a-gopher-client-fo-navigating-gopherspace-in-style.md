---
id: "intr-gophyr-building-a-gopher-client-fo-navigating-gopherspace-in-style"
type: "concept"
domain: "debug"
title: "Gophyr: Building a Gopher Client for Zephyr with Claude: Navigating Gopherspace in style"
summary: "With Gophyr compiled and running on the nRF7002-DK, it's time to take it out for a spin on the Route 66 of the Information Superhighway. Let's fire up the serial terminal and explore this historic digital landscape."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-05-16-gophyr-gopher-for-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/gophyr-gopher-for-zephyr#navigating-gopherspace-in-style"
license: "CC-BY-SA-4.0"
mode: "V"
---

With Gophyr compiled and running on the nRF7002-DK, it's time to take it out for
a spin on the _Route 66 of the Information Superhighway_. Let's fire up the
serial terminal and explore this historic digital landscape.

Gopherspace is one of those early digital neighborhoods you might be surprised
still exists. (Remember, shortwave radio is
[still a thing](https://hackaday.com/blog/?s=shortwave) too!) It's an alternate
web where content is organized by type and server, not chaotically linked like
today's "surface web." Here you'll find text files (lots of them), directory
menus, search interfaces, and proxies to popular www services.

With Gophyr running on our shiny MCU board, we can use the following Gopher
client commands to navigate this space in style:

```plaintext
uart:~$ gopher
Gopher Client Commands:
----------------------
gopher ip - Display network information
gopher connect <host> [port] - Connect to a Gopher server
gopher get [selector] - Request a document or directory
gopher view <index> - View an item from the directory
gopher back - Navigate back to previous item
gopher search <index> <search_string> - Search using a search server
gopher help - Display this help message
uart:~$
```

SDF.org is a great place to start our Gopher journey:
([sign up for a shell account](https://sdf.org/?signup), while you're at it,
eh?)

(figure: sdf.org in full-color Gophyr, running on an nRF7002-DK)

### Notable Destinations

Beyond SDF, we can navigate to several interesting Gopher servers still
operational today:

#### **Floodgap Systems** (gopher.floodgap.com)

```plaintext
shell> gopher connect gopher.floodgap.com

Welcome to Floodgap Systems' official gopher server.
Floodgap has served the gopher community since 1999
(formerly gopher.ptloma.edu).

We run Bucktooth 0.2.9 on xinetd as our server system.
gopher.floodgap.com is an IBM Power 520 Express with a 2-way
4.2GHz POWER6 CPU and 8GB of RAM, running AIX 6.1 +patches.
Send gopher@floodgap.com your questions and suggestions.

***********************************************************
**              OVER 20 YEARS SERVING YOU!               **
**               Plain text is beautiful!                **
***********************************************************

1: [DIR] Does this gopher menu look correct?
(plus using the Floodgap Public Gopher Proxy)
2: [DIR] Are you running a bot? Are we blocking you?
Please read this document. Please don't cost us money.
3: [DIR] Super-Dimensional Fortress: SDF Gopherspace
Get your own Gopherspace and shell account!

...
```

#### **HN Gopher - A Hacker News Mirror**

```plaintext
shell> gopher connect hngopher.com
    _    _            _               _   _
    | |  | |          | |             | \ | |  hngopher.com:70
    | |__| | __ _  ___| | _____ _ __  |  \| | _____      _____
    |  __  |/ _` |/ __| |/ / _ \ '__| | . ` |/ _ \ \ /\ / / __|
    | |  | | (_| | (__|   <  __/ |    | |\  |  __/\ V  V /\__ \
    |_|  |_|\__,_|\___|_|\_\___|_|    |_| \_|\___| \_/\_/ |___/

              - The Underground Hacker News Mirror
                        (updated hourly)

                              _________________
                              |\                \
                              | \                \
                _     _      |\ \________________\
                (>\---/<)     |\\ |      ____     |
                ,'     `.     |.\ |     |\   \    |
              /  q   p  \    |   |     |.\   \___|____
              (  >(_Y_)<  )    \  |     ||\\   \       \
              >-' `-' `-<-.    \ |     || \\___\       \
              /  _.,,  ,,,- \    \|_____||  ||  !\_______\
            /,    )`  '(    )   ______ ||  ||  !  . . . |
            ; `._.'      `--<    \000  \~\\ ||  !   . .  |
          :     \        |  )    \000 9\ \\||  !    .   |
          \      )       ;_/      \000 9\ \.|  !        |
            `._ _/_  ___.'-'''      \000 9\ \|__!________/
              `--'''                ^^^^^`` \/_____\
                                        hjw/hectoras/mozz
________________________________________________________________
This is a mirror of the popular tech news aggregator Hacker News
(https://news.ycombinator.com). All stories and discussions have
been converted to plain-text ASCII. Have fun exploring the site!
________________________________________________________________

1: [DIR] Live Feed
  (last update 2025-05-12 21:02:10 UTC)

...

```
