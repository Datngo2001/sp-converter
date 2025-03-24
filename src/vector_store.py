from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

vector_store = Chroma(
    embedding_function=embeddings,
    collection_name="sp_converter_collection",
    persist_directory="/home/datngominh/sp-converter/vector_store",
)