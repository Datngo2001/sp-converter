from ollama import chat
from ollama import ChatResponse

def generate_text(input: str) -> str:
    response: ChatResponse = chat(
      model="hf.co/lmstudio-community/Phi-3.1-mini-4k-instruct-GGUF:IQ4_XS", 
      messages=[
        {
            'role': 'user',
            'content': input,
        },
      ]
    )
    return response['message']['content']