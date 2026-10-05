<!-- Append to .github/copilot-instructions.md (or AGENTS.md) in a CMSIS project. -->
## CMSIS knowledge base

For questions or errors around CMSIS, csolution, cbuild, cpackget, packchk, svdconv, pyOCD or Pack development:

1. Call `knowledge_search` with the exact error text or the question. Pass `cbuild` = path to the active `*.cbuild.yml` so results match the device, components and compiler of this project.
2. Call `knowledge_get` for the best hit before acting. Procedures are complete; follow them including their stop conditions and user confirmations.
3. Use `knowledge_expand` to find prerequisites (`requires`) and related Pack documentation.
4. Results marked `"applies": "unverified"` may not match this target; say so to the user.
