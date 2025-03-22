from rag_pipeline import graph

# Test the application
print("Testing the application...")

response = graph.invoke({"question": "What is [dbo].[DatabaseLog]?"})
print(response["answer"])