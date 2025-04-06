from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Current embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Uncomment one of the following embedding models for code-specific tasks:

# CodeBERT: Best for code search, summarization, and understanding code semantics
# embeddings = HuggingFaceEmbeddings(model_name="microsoft/codebert-base")

# GraphCodeBERT: Best for deeper understanding of code structure and data flow
# embeddings = HuggingFaceEmbeddings(model_name="microsoft/graphcodebert-base")

# CodeT5: Best for code generation, summarization, and translation
# embeddings = HuggingFaceEmbeddings(model_name="Salesforce/codet5-base")

# CodeGen: Best for code generation and embeddings for programming tasks
# embeddings = HuggingFaceEmbeddings(model_name="Salesforce/codegen-350M-mono")

# StarCoder: General-purpose code understanding and embeddings for multiple programming languages
# embeddings = HuggingFaceEmbeddings(model_name="bigcode/starcoder")

vector_store = Chroma(
    embedding_function=embeddings,
    collection_name="sp_converter_collection",
)