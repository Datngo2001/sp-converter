from langchain_core.documents import Document
from langchain import hub
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

from llm_model import llm, sampling_params
from vector_store import vector_store

# Define prompt for question-answering
prompt = hub.pull("rlm/rag-prompt")

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
        "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\n"
        f"Question: {question}\n"
        f"Context: {context}\n"
        "Answer:"
    )
    return prompt_str

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = create_prompt(state["question"], docs_content)
    response = llm.generate(messages, sampling_params)
    return {"answer": response[0].outputs[0].text}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()