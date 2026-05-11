import json
from Agents.ResearcherAgent import *
from Agents.SummariserAgent import *
from datapizza.memory import Memory
from datapizza.tools.mcp_client import MCPClient
import os

memory = Memory()

mcp_client = MCPClient(url="http://127.0.0.1:8000/mcp")

fastmcp_tools = mcp_client.list_tools()


with open("news_article_collection_config.json") as f:
    newsConfig = json.load(f)

print("Country Selected " + newsConfig["country"])

researcherAgent = ResearcherAgent(memory, newsConfig)

summariserAgent = SummariserAgent(memory, newsConfig, fastmcp_tools)

summariserAgent.can_call(researcherAgent)

# researcherResponse = researcherAgent.run()

result = summariserAgent.run()
print(result)