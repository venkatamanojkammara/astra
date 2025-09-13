from all_tools import tools
from langchain.agents import initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


def create_agent():
    """Initialize Gemini agent with all tools."""
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    
    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    return agent


agent = create_agent()

def run_agent_command(command: str) -> str:
    """Run a natural language command through the agent."""
    try:
        response = agent.run(command)
        return str(response)
    except Exception as e:
        return f"Error: {e}"