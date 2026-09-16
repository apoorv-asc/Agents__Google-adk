from google.adk.agents.llm_agent import Agent

joke_agent = Agent(
    model='gemini-3.5-flash',
    name='joke_agent',
    description='an agent which creates jokes.',
    instruction='Tell me a joke when asked',
)
