from state import SquadState

def router_logic(state: SquadState) -> str:
    feedback = state.get("feedback", "")
    iterations = state.get("iterations", 0)
    
    print(f"\n[Router] Current Iterations: {iterations}")
    
    if iterations >= 3:
        print("[Router] Max iterations reached. Ending workflow.")
        return "end"
        
    if "APPROVED" in feedback.upper():
        print("[Router] Code approved! Ending workflow.")
        return "end"
    else:
        print("[Router] Code needs work. Routing back to Developer.")
        return "developer"