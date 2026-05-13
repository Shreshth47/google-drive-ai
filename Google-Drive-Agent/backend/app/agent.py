import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

from .tools import search_google_drive

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_retries=2
)
tools = [search_google_drive]
llm_with_tools = llm.bind_tools(tools)

def call_model(state: MessagesState):
    """Calls the LLM with the current conversation history."""
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode(tools))
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    tools_condition,
    {
        "tools": "tools",
        END: END          
    }
)

workflow.add_edge("tools", "agent")
agent_executor = workflow.compile()
