from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

class SummariserAgent(Agent):
    def __init__(self, _memory, config):
        
        self.language = config["language"]

        _system_prompt = ( "You are a web news articler summariser. " \
        "You receive web URLS to news articles about a given topic to read through and summarise in details the topic and events. " \
        "You will output a summary of all the information gathered from the articles to explain what is being discussed for further assessment. "\
        "The summary will need to include source references"
        )

        super().__init__(
            name="Summary Agent",
            system_prompt = _system_prompt,
            client=OpenAIClient(api_key="OpenAI API Key", model="gpt-4.1"),
            # tools=[],
            max_steps=3,
            terminate_on_text=True,
            stateless=False,
            memory=_memory,
        )

        print(f"{self.name} agent has come online")

    def run(self):
        return super().run(f"Create a summary for a collection of web articles collected by the ResearcherAgent. Your summary should be written in the {self.language} language")