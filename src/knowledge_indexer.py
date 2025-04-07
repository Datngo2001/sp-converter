from langchain_community.document_loaders import FileSystemBlobLoader
from vector_store import vector_store
import os
import chardet
from langchain_core.documents import Document

# Load and index knowledge base
path = "/home/datngominh/sp-converter/knowledge_base"
glob_pattern = "**/[!.]*"
loader = FileSystemBlobLoader(path=path, glob=glob_pattern)

print(f"Checking path: {path}")
print(f"Using glob pattern: {glob_pattern}")
print(f"Absolute path: {os.path.abspath(path)}")
print(f"Directory exists: {os.path.isdir(path)}")

# Ask for user confirmation before clearing existing documents
confirm = input("Do you want to clear existing documents in the vector store? (yes/no): ").strip().lower()
if confirm == 'yes':
    print("Clearing existing documents in the vector store...")
    vector_store.reset_collection()
    print("Existing documents cleared.")
else:
    print("Skipping clearing of existing documents.")

print("Indexing knowledge base...")
total_files = loader.count_matching_files()
print(f"Found {total_files} files to index.")

indexed_files = 0
for blob in loader.yield_blobs():
    file_content = blob.as_bytes()
    encoding = chardet.detect(file_content)['encoding']
    if encoding is None:
        print(f"Could not detect encoding for file: {blob.path}")
        continue
    
    try:
        file_text = file_content.decode(encoding)
        
        sql_command = file_text.replace("SET ANSI_NULLS ON\r\nGO\r\nSET QUOTED_IDENTIFIER ON\r\nGO", "")
        
        _ = vector_store.add_documents(
            documents=[Document(page_content=sql_command)],
            identifiers=[blob.path],
        )
        indexed_files += 1
        print(f"{indexed_files}/{total_files} files indexed.")
    except Exception as e:
        print(f"Error decoding file {blob.path} with encoding {encoding}: {e}")

print("Knowledge base indexed.")
