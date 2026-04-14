from typing import TypedDict

class SquadState(TypedDict):
    task: str           # The original user request
    plan: str           # The step-by-step plan created by the Planner
    code: str           # The code written by the Developer
    feedback: str       # The review notes from the Reviewer
    iterations: int     # Counter to prevent infinite loops