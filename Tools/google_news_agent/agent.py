from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-3.5-flash',
    # model = 'gemini-2.5-flash',
    name='root_agent',
    instruction='Look for all the latest news in the internet and provide a crisp summary based on the topic.',
    description='An agent that uses Google Search to fetch up-to-date news',
)
