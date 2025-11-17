from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

class ResearcherAgent(Agent):
    def __init__(self, _memory, config):
        
        self.maxNumberOfArticles = config["MaxNumberOfArticles"]
        self.country = config["country"]
        self.topic = config["topic"]

        _system_prompt = ( "You are a web news article researcher" \
        "You scrape the internet to find the most up to date news articles from reliable sources" \
        "Record the URLS only in a JSON format to be used by a summariser agent"
        f"Find a maximum of {self.maxNumberOfArticles} articles, use only {self.country} based sources on the topic of {self.topic}"
        )

        super().__init__(
            name="ResearcherAgent",
            system_prompt = _system_prompt,
            client=OpenAIClient(api_key="OpenAI API Key", model="gpt-4.1-mini"),
            # tools=[],
            max_steps=3,
            terminate_on_text=True,
            stateless=False,
            memory=_memory,
        )

        print(f"{self.name} agent has come online")

    def run(self):
        return super().run(f"Find a maximum of {self.maxNumberOfArticles} articles in {self.country} on the topic of {self.topic}")



    