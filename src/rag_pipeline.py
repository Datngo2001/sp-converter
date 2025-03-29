from langchain_core.documents import Document
from langchain import hub
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

from llm_model import generate_text
from vector_store import vector_store

# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

# Define application steps
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def create_prompt(question: str, context: str):
    prompt_str = (
        "You are a highly skilled assistant specializing in SQL Server databases, C#, Entity Framework Core, and .NET Core development.\n"
        "Your task is to generate accurate and efficient C# code based on the provided context and task description.\n"
        "Use the following retrieved context to perform the task. If the context is insufficient or you are unsure, respond with 'I don't know'.\n"
        "Ensure the code adheres to best practices and is production-ready.\n\n"
        f"Task Description: {question}\n"
        f"Retrieved Context:\n{context}\n\n"
        "Generated C# Code:"
    )
    return prompt_str

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = create_prompt(state["question"], docs_content)
    response = generate_text(messages, max_length=2000)
    return {"answer": response}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()