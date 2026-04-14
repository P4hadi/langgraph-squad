# 🤖 LangGraph Multi-Agent Coding Squad

An autonomous, multi-agent artificial intelligence system built with **LangGraph** and powered by **Google's Gemini 2.5 Flash**. This system simulates a professional software development team to break down complex tasks, write code, and review it for quality assurance.

## 🏗️ Architecture & Agents

The system utilizes a cyclic graph state machine where specialized AI agents collaborate through shared memory (`SquadState`).

1. **🧠 The Planner:** Acts as the Senior Architect. It takes the user's raw prompt and breaks it down into a logical, step-by-step implementation plan without writing any code.
2. **💻 The Developer:** Acts as the Software Engineer. It reads the architectural plan and generates clean, executable Python code. 
3. **🧐 The Reviewer:** Acts as the QA/Code Reviewer. It analyzes the generated code against the original request. If bugs or missing features are found, it generates feedback and routes the state back to the Developer. If the code is perfect, it outputs "APPROVED".
4. **🔀 The Router (Conditional Edge):** Evaluates the Reviewer's feedback to either terminate the graph successfully or loop back to the Developer for revisions (with a built-in iteration limit to prevent infinite loops).

## 🛠️ Tech Stack
* **Framework:** [LangGraph](https://python.langchain.com/docs/langgraph) / LangChain
* **LLM:** Google Gemini 2.5 Flash
* **Language:** Python 3.x

## 🚀 Getting Started

### Prerequisites
* Python 3.9 or higher
* A free [Google AI Studio API Key](https://aistudio.google.com/app/apikey)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/P4hadi/langgraph-squad.git](https://github.com/P4hadi/langgraph-squad.git)
   cd langgraph-squad
