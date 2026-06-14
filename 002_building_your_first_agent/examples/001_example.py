from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()


agent = Agent(
    name="HelperBot",
    instructions="You are a helpful assistant. Answer questions clearly.",
)

user_input = "What is the capital of France?"

result = Runner.run_sync(agent, user_input)
print(result.final_output)
