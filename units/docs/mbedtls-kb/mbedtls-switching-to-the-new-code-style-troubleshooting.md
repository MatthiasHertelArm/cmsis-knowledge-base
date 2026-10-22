---
id: "mbedtls-switching-to-the-new-code-style-troubleshooting"
type: "concept"
domain: "security"
title: "Switching to the new code style: Troubleshooting"
summary: "If all did not go well, please re-run the script with the --verbose option and read the output to see what went wrong."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/rewrite-branch-for-coding-style.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/rewrite-branch-for-coding-style.md#troubleshooting"
license: "Apache-2.0"
mode: "V"
---

### If something goes wrong

If all did not go well, please re-run the script with the `--verbose` option and read the output to see what went wrong. If you can't figure it out, please post on the [mbed-tls mailing list](https://lists.trustedfirmware.org/mailman3/lists/mbed-tls.lists.trustedfirmware.org/) or raise an issue on the [mbedtls-docs repository](https://github.com/Mbed-TLS/mbedtls-docs/issues), including a link to the problematic branch and the **complete output from `mbedtls-rewrite-branch-style --verbose`**.

### Cleaning up after an error run

The script works in a temporary worktree following the pattern `tmp-%s-%d` where `%s` is the name of the branch being rewritten. If there is an error, this worktree is left behind. Use the command `git worktree list` to list existing worktrees. The following command shows output reduced worktrees that are probably from the branch rewriting script:
```console
$ git worktree list | grep /tmp-
/home/me/work/tmp-mybranch-1234
```
Use `git worktree remove -f /home/me/work/tmp-mybranch-1234` to remove the worktree.

### Git rebase fails

The rewrite script starts by rebasing the given branch on top of the last upstream commit before the code style change. If there is a conflict, the script fails:
```
subprocess.CalledProcessError: Command '['git', 'rebase', '449bd8303eed8164b83682d2ce028dca0e49b1fa~1']' returned non-zero exit status 1.
```

In this case, please do the rebase manually and resolve the conflicts, then run the rewrite script again.

### Wrong version of uncrustify

If you see the message
```
Unsupported version of uncrustify. This script needs 0.75.1.
```
please install the requested version of uncrustify. Unfortunately, different versions give different outputs, so everyone needs to use the same version.

If you have multiple versions of uncrustify installed, please make sure that the requested version comes first in the command search path (`$PATH` or `%PATH%`).

### Backup branch out of date

By default, the script backs up the old state of the branch under a name beginning with `old-code-style/`. If you run the rewrite script on a branch, then do more work on that branch, then run the rewrite script again, the script will fail with an error:
```
fatal: A branch named 'old-code-style/mybranch' already exists.
```
Please remove the old backup branch manually, then run the script again.
