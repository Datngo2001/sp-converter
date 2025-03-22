from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

vector_store = Chroma(embedding_function=embeddings)


def get_document_count():
    return vector_store

# Example usage
if __name__ == "__main__":
    print(f"Number of documents in vector_store: {get_document_count()}")