import os
from dotenv import load_dotenv

# 1. LOAD THE API KEY FIRST!
load_dotenv()

from langgraph.graph import StateGraph, END

# 2. NOW IMPORT YOUR AGENTS
from state import SquadState
from router import router_logic
from agents.planner import planner_agent
from agents.developer import developer_agent
from agents.reviewer import reviewer_agent

# Initialize the graph
workflow = StateGraph(SquadState)


# 2. Add nodes (agents)
workflow.add_node("planner", planner_agent)
workflow.add_node("developer", developer_agent)
workflow.add_node("reviewer", reviewer_agent)

# 3. Add edges (connections)
workflow.set_entry_point("planner")
workflow.add_edge("planner", "developer")
workflow.add_edge("developer", "reviewer")

# 4. Add conditional routing
workflow.add_conditional_edges(
    "reviewer",
    router_logic,
    {
        "end": END,
        "developer": "developer"
    }
)

# 5. Compile the app
app = workflow.compile()

if __name__ == "__main__":
    print("Welcome to the Modular LangGraph Squad!")
    user_task = input("What would you like the agents to build? \n> ")
    
    initial_state = {
        "task": user_task,
        "plan": "",
        "code": "",
        "feedback": "",
        "iterations": 0
    }
    
    print("\nStarting workflow...")
    final_state = app.invoke(initial_state)
    
    print("\n=========================================")
    print("🎉 FINAL OUTPUT 🎉")
    print("=========================================")
    print(final_state["code"])