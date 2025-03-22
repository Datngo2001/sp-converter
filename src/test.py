from rag_pipeline import graph

response = graph.invoke({"question": "What is [dbo].[DatabaseLog]?"})
print(response["answer"])