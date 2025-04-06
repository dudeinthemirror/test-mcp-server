# test-mcp-server

## Development
### Install uv
This project uses the `uv` packager. To install it on your machine, run:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install direnv
This project uses `direnv` to load and unload environment variables depending on the current directory
```shell
brew install direnv
```
First time you cd into this project you will be prompted to run:
```shell
direnv allow
```

### Dependencies
To install dependencies, run:
```shell
uv sync
```

### Linting, formatting
This project uses `ruff`. Ruff is written in Rust, designed to be extremely fast and efficient

```shell
# Lint files or directories
ruff check ./src

# Format files
ruff format ./src

# Fix issues automatically
ruff check --fix ./src
```
- (optional) in VSCode you can install the Ruff extension (+ uninstall Black)


### Running and debugging
- start the server in dev mode
```shell
uv run fastapi dev src/main.py --host 127.0.0.1 --port 8088
```
OR,
```shell
uv run fastapi dev src/simple_integration.py --host 127.0.0.1 --port 8088
```

- start the MCP inspector
```shell
npx @modelcontextprotocol/inspector http://127.0.0.1:8088/mcp
```
- open the inspector in the browser `http://127.0.0.1:5173`
- in the left panel:
  - Transport Type: SSE
  - URL: `http://127.0.0.1:8088/mcp`
  - click on `Connect`