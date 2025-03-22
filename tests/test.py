from rag_pipeline import graph

response = graph.invoke({"question": "What is Task Decomposition?"})
print(response["answer"])