from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from state import SquadState

# Initialize the free Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

def developer_agent(state: SquadState):
    print("\n--- 💻 DEVELOPER AGENT WORKING ---")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Python developer. Write the code based on the provided plan. If there is feedback from a reviewer, incorporate it to fix the code. ONLY output the Python code, no markdown formatting or explanations."),
        ("user", "Original Task: {task}\n\nImplementation Plan: {plan}\n\nPrevious Feedback: {feedback}\n\nCurrent Code: {code}")
    ])
    chain = prompt | llm
    response = chain.invoke({
        "task": state["task"],
        "plan": state["plan"],
        "feedback": state.get("feedback", "None yet."),
        "code": state.get("code", "No code written yet.")
    })
    
    current_iterations = state.get("iterations", 0) + 1
    return {"code": response.content, "iterations": current_iterations}