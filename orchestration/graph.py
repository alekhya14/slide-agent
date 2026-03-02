from agents.planner_agent import plan_deck
from agents.codegen_agent import execute_deck
from agents.validator_agent import validate_deck


def run_pipeline(prompt: str):
    deck_spec = plan_deck(prompt)

    errors = validate_deck(deck_spec)
    if errors:
        raise ValueError(f"Validation failed: {errors}")

    output_path = execute_deck(deck_spec)
    return output_path