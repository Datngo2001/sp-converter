from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import FileSystemBlobLoader
from vector_store import vector_store
import os
import chardet

# Load and index knowledge base
path = "/home/datngominh/sp-converter/knowledge_base"
glob_pattern = "*.sql"
loader = FileSystemBlobLoader(path=path, glob=glob_pattern)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

print(f"Checking path: {path}")
print(f"Using glob pattern: {glob_pattern}")
print(f"Absolute path: {os.path.abspath(path)}")
print(f"Directory exists: {os.path.isdir(path)}")

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
        all_splits = text_splitter.create_documents([file_text])
        _ = vector_store.add_documents(
            documents=all_splits,
            identifiers=[blob.path],
        )
        indexed_files += 1
        print(f"{indexed_files}/{total_files} files indexed.")
    except Exception as e:
        print(f"Error decoding file {blob.path} with encoding {encoding}: {e}")

print("Knowledge base indexed.")
