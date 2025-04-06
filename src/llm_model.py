from ollama import chat
from ollama import ChatResponse
from typing import List

def generate_text(inputs: List[str] ) -> str:
  user_messages = []
  for input in inputs:
    user_messages.append({
      'role': 'user',
      'content': input,
    })
  
  response: ChatResponse = chat(
    model="hf.co/lmstudio-community/Phi-3.1-mini-4k-instruct-GGUF:IQ4_XS", 
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
    }
  )
  return response['message']['content']