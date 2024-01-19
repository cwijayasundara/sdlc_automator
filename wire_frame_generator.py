from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, load_tools

load_dotenv()

llm = ChatOpenAI(model="gpt-4-1106-preview",
                 streaming=True)

tools = load_tools(["dalle-image-generator"])

agent = initialize_agent(tools,
                         llm,
                         agent="zero-shot-react-description",
                         verbose=True)

output = agent.run("Generate a UI mock up for a banking customer registration page. Use English language!!")
print(output)
