from openai import OpenAI
import os
import json

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
from schemas.slide_spec import DeckSpec

SYSTEM_PROMPT = """
You are a presentation planning agent.

Your job is to convert a user request into a structured slide plan.

Always call the function `create_deck`.
Never respond with text.
"""

tools = [
    {
        "type": "function",
        "function": {
            "name": "create_deck",
            "description": "Create a structured presentation plan",
            "parameters": {
                "type": "object",
                "properties": {
                    "slides": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "bullets": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                },
                                "chart": {
                                    "type": ["object", "null"],
                                    "properties": {
                                        "type": {"type": "string"},
                                        "title": {"type": "string"},
                                        "categories": {
                                            "type": "array",
                                            "items": {"type": "string"}
                                        },
                                        "values": {
                                            "type": "array",
                                            "items": {"type": "number"}
                                        }
                                    },
                                    "required": ["type", "title", "categories", "values"]
                                }
                            },
                            "required": ["title", "bullets"]
                        }
                    }
                },
                "required": ["slides"]
            }
        }
    }
]

def plan_deck(user_prompt: str) -> DeckSpec:
    response = client.chat.completions.create(model="gpt-4o-mini",
    temperature=0,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "create_deck"}}
    )

    # content = response.choices[0].message.content

    # data = json.loads(content)
    # return DeckSpec(**data)
    tool_call = response.choices[0].message.tool_calls[0]
    arguments = tool_call.function.arguments

    return DeckSpec.model_validate_json(arguments)

# def plan_deck(user_prompt: str) -> DeckSpec:
#     response = openai.ChatCompletion.create(
#         model="gpt-4o-mini",
#         temperature=0,
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user", "content": user_prompt}
#         ],
#         tools=tools,
#         tool_choice={"type": "function", "function": {"name": "create_deck"}}
#     )
#
#