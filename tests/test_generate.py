import sys
import os

# Get the absolute path of the utils directory
sys.path.append(os.path.abspath("src"))

from rag_pipeline import graph

# Test the application
print("Testing the application...")

response = graph.invoke({"question": """
    SELECT [AddressID]
      ,[AddressLine1]
      ,[AddressLine2]
      ,[City]
      ,[StateProvinceID]
      ,[PostalCode]
      ,[SpatialLocation]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [Person].[Address]
"""})

print("Answer:")

# Write the answer to a text file
with open("response_answer.txt", "w") as file:
    file.write(response["answer"])

print("Test complete.")