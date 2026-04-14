from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from state import SquadState

# Initialize the free Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

def planner_agent(state: SquadState):
    print("\n--- 🧠 PLANNER AGENT WORKING ---")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a senior software architect. Break down the user's task into a clear, step-by-step implementation plan. Do NOT write code, only write the plan."),
        ("user", "Task: {task}")
    ])
    chain = prompt | llm
    response = chain.invoke({"task": state["task"]})
    
    return {"plan": response.content, "iterations": state.get("iterations", 0)}