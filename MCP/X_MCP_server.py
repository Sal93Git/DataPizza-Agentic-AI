from fastmcp import FastMCP
import requests

# BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
BEARER_TOKEN = f"test_only"

mcp = FastMCP("DataPizza_Agent_MCP")

@mcp.tool
def getUserName():
    """A function get the current users name"""
    print("MCP Func called !!!!")
    return "Mr Mega Cheesy Pizza"

@mcp.tool
def get_x_posts(query: str, max_results: int = 10) -> list[str]:
    """
    Fetch recent X posts for a query and return tweet text list.
    """

    url = "https://api.x.com/2/tweets/search/recent"

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    params = {
        "query": query,
        "max_results": 10,
        "tweet.fields": "created_at,lang,public_metrics"
    }

    res = requests.get(url, headers=headers, params=params)

    if res.status_code != 200:
        return [f"Error: {res.status_code} - {res.text}"]

    data = res.json()

    return [
        tweet["text"]
        for tweet in data.get("data", [])
    ]


if __name__ == "__main__":
    print("MCP Server Coming Online")
    mcp.run(transport="http", host="127.0.0.1", port=8000)
