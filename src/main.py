from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi_mcp import add_mcp_server


# Create a new FastAPI app instance
app = FastAPI(description="Test MCP server")

# Mount the MCP server
add_mcp_server(
    app,
    mount_path="/mcp",  # Where to mount the MCP server
    name="Test MCP Server",
)


# -------------------------------
# ROUTES
# -------------------------------
@app.get("/")
def read_root():
    """
    Returns a simple "Up" status message
    """
    return {"status": "Up"}


@app.get("/list_agents")
def list_agents() -> dict:
    return {
        "agents": [
            {"name": "AG1", "description": "Agent 1"},
            {"name": "AG2", "description": "Agent 2"},
            {"name": "AG3", "description": "Agent 3"},
            {"name": "AG4", "description": "Agent 4"},
        ]
    }

