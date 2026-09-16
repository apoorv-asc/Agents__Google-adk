from google.adk.agents.llm_agent import Agent
from .subagents.joke import joke_agent
from .subagents.news import news_agent
from google.adk.tools.agent_tool import AgentTool

root_agent = Agent(
    model='gemini-3.5-flash',
    name='entertainment_agent',
    description='You are an entertainer agent which tells me a joke or a news when asked',
    instruction='You are an entertainer agent which uses other agents to tell news or a joke' \
    'Intructions : ' \
    ' - Please greet the user and offer the services you provide and ask for thier choice' \
    ' - Based on users preference use the sub agents to get the output and present them to the user.',

    # Using sub_agents as sub agents
    # sub_agents = [ joke_agent, news_agent]

    # Using sub_agents as tools
    tools = [
        AgentTool(agent = news_agent),
        AgentTool(agent = joke_agent)
    ]
)
