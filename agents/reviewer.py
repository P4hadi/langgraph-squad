from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from state import SquadState

# Initialize the free Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

def reviewer_agent(state: SquadState):
    print("\n--- 🧐 REVIEWER AGENT WORKING ---")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a strict code reviewer. Review the provided Python code against the original task. If the code is perfect and complete, reply exactly with the word 'APPROVED'. If it has bugs or is missing features, provide specific feedback on what needs to be fixed."),
        ("user", "Original Task: {task}\n\nCode to Review:\n{code}")
    ])
    chain = prompt | llm
    response = chain.invoke({
        "task": state["task"],
        "code": state["code"]
    })
    
    return {"feedback": response.content}