from google.adk.agents.llm_agent import Agent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool

scrape_news_tool = CrewaiTool(
    name = "scrape_groww",
    description = "Scrapes the latest information about stocks and mutual funds listed on Groww",
    tool = ScrapeWebsiteTool("https://groww.in/")
)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='scrape_groww',
    description='An agent for stock and mutual fund related information',
    instruction='provides the latest information regarding stocks and mutual funds using the tool provided',
    tools = [scrape_news_tool]
)
