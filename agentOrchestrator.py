import json
from Agents.ResearcherAgent import *
from Agents.SummariserAgent import *
from datapizza.memory import Memory

memory = Memory()


with open("news_article_collection_config.json") as f:
    newsConfig = json.load(f)

print("Country Selected " + newsConfig["country"])

researcherAgent = ResearcherAgent(memory, newsConfig)

summariserAgent = SummariserAgent(memory, newsConfig)

summariserAgent.can_call(researcherAgent)

# researcherResponse = researcherAgent.run()

result = summariserAgent.run()
print(result)