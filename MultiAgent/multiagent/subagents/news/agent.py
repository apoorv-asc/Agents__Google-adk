from google.adk.agents.llm_agent import Agent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool


scrape_news_tool = CrewaiTool(
    name = "scrape_news",
    description = "Scrapes the latest news and return me a short summary if user asks about some specific topic. If in case he asks for multiple topics, give them 2-3 points.",
    tool = ScrapeWebsiteTool("https://www.aajtak.in/")
)

news_agent = Agent(
    model='gemini-3.5-flash',
    name='news_agent',
    description='An agent for getting latest news',
    instruction='Scrapes the latest news and return me a short summary if user asks about some specific topic. If in case he asks for multiple topics, give them 2-3 points.',
    tools = [scrape_news_tool]
)
