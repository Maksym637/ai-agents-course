from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool

load_dotenv()


def main():
    agent = Agent(
        name="Web Search Agent",
        tools=[WebSearchTool()],
        instructions=(
            "You are a web search agent. "
            "You can use the web search tool to find information on the web."
        ),
    )

    user_input = "Latest news about AI"

    result = Runner.run_sync(agent, user_input)
    print(result.final_output)


if __name__ == "__main__":
    main()
