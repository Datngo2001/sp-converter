from knowledge_loader import KnowledgeLoader
from llm_model import llm, sampling_params
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from vector_store import vector_store
    
from langchain import hub
from langchain_community.document_loaders import FileSystemBlobLoader
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict


# Load and index knowledge base
loader = FileSystemBlobLoader(path="./knowledge_base", glob="**/*.txt")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

for blob in loader.yield_blobs():
    all_splits = text_splitter.create_documents([blob.as_string()])
    _ = vector_store.add_documents(documents=all_splits)

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


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.generate(messages, sampling_params)
    return {"answer": response[0].outputs[0].text}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()