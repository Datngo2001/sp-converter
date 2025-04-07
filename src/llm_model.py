from ollama import chat as ollama_chat
from ollama import ChatResponse
from typing import List
from llm_tools import create_cs_file

tools = [
  {"create_cs_file": create_cs_file}
]

def chat(inputs: List[str]) -> ChatResponse:  
  user_messages = []
  for input in inputs:
    user_messages.append({
      'role': 'user',
      'content': input,
    })
  
  response: ChatResponse = ollama_chat(
    model="llama3.2", 
    messages=[
      {
          'role': 'system',
          'content': 'You are an AI assistant specialized in programming tasks. Provide concise and accurate code suggestions.',
      },
      *user_messages
    ],
    options={
      "temperature": 0.2,  # Lower temperature for deterministic and precise outputs
      "max_tokens": 512,   # Limit the response length to avoid overly verbose outputs
      "top_p": 0.9,        # Use nucleus sampling for better quality
      "frequency_penalty": 0.1,  # Slight penalty to discourage repetitive outputs
      "presence_penalty": 0.0    # Neutral presence penalty
    },
    tools=tools,
  )

  return response

def generate_text(inputs: List[str] ) -> str:
  """
  Generate text using the LLM model.
  """
  response = chat(inputs)
  return response["message"]["content"]


def generate_response(inputs: List[str]) -> ChatResponse:
  """
  Generate a response using the LLM model.
  """
  response = chat(inputs)
  return response