from typing import Any
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, Runner, RunContextWrapper, FunctionTool

load_dotenv()


def file_read_tool(data):
    """Custom tool function that can be called by the agent."""
    with open(data, "r") as file:
        result = file.readlines()

    return result


class FunctionArgs(BaseModel):
    file_path: str


async def run_function(ctx: RunContextWrapper[Any], args: str) -> str:
    parsed = FunctionArgs.model_validate_json(args)
    return str(file_read_tool(parsed.file_path))


custom_tool = FunctionTool(
    name="custom_tool",
    description="A custom tool that can be called by the agent.",
    params_json_schema={
        "type": "object",
        "properties": {
            "file_path": {"type": "string"},
        },
        "required": ["file_path"],
        "additionalProperties": False,
    },
    on_invoke_tool=run_function,
)


def main():
    agent = Agent(
        name="File Read Agent",
        tools=[custom_tool],
    )

    user_input = "Read the file ./data/data.txt"

    result = Runner.run_sync(agent, user_input)
    print(result.final_output)


if __name__ == "__main__":
    main()
