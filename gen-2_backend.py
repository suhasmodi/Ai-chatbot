from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv
import uvicorn
from langchain_groq.chat_models import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langserve import add_routes

# Load environment variables
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize FastAPI app
app = FastAPI(title="LangGraph AI Agent")

# Define request data model
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

# Initialize AI model
model = ChatGroq(model='llama-3.3-70b-versatile')

# Initialize search tool
search_tool = TavilySearchResults(max_result=2)

# Define AI agent with a behavior prompt
prompt = "You are a helpful AI assistant. Respond to user queries in a concise and informative manner act like harry potter"

# Create AI agent with tools
agent = create_react_agent(model=model, tools=[search_tool], prompt=prompt)

# Define API endpoint to get AI response
@app.post("/get_ans/invoke")
async def get_ans(request: ChatRequest):
    try:
        # Convert messages into the expected format
        chat_history = [{"role": msg.role, "content": msg.content} for msg in request.messages]

        # Invoke the agent
        response = agent.invoke({"messages": chat_history})

        # Return AI response
        return {"content": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add routes for additional models or agents
add_routes(app, model, path='/meta-llama')
add_routes(app, agent, path='/get_ans')

# Run FastAPI application
if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=3000)
