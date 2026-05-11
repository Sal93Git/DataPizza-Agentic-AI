from fastmcp import FastMCP

mcp = FastMCP("DataPizza_Agent_MCP")

@mcp.tool
def getUserName():
    """A function get the current users name"""
    print("MCP Func called !!!!")
    return "Mr Mega Cheesy Pizza"


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
    print("MCP Server online")
