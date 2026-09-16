from google.adk.agents.llm_agent import Agent

def add_numbers(a : float , b : float) -> float :
    """ Add two numbers and return the result. """
    return a + b;

def multiply_numbers(a : float , b : float) -> float :
    """ Add two numbers and return the result. """
    return a * b;

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    instruction='Perform addition or multiplication based on user request. Use the tools provided based on user prompt. If no input is given, ask for input numbers.',
    description='An agent that performs mathematical calculation based on user\'s request.',
    tools = [add_numbers,multiply_numbers]
)
