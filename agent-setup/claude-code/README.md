# Claude Code

    claude mcp add cmsis-knowledge -- /ABSOLUTE/PATH/cmsis-knowledge-base/.venv/bin/python \
        /ABSOLUTE/PATH/cmsis-knowledge-base/tools/kb_server.py \
        /ABSOLUTE/PATH/cmsis-knowledge-base/build/knowledge.db

Then add the text of `../vscode/copilot-instructions.md` to the project's `CLAUDE.md`.

Other MCP clients (Cline, Continue, agents driving local models via Ollama) use the same
command and arguments in their MCP server configuration.
