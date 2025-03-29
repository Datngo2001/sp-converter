from functools import cache
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(
    "deepseek-ai/deepseek-coder-1.3b-base", 
    trust_remote_code=True,
    cache_dir="/home/datngominh/sp-converter/models",
)

model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/deepseek-coder-1.3b-base", 
    trust_remote_code=True,
    cache_dir="/home/datngominh/sp-converter/models",
).cuda()

def generate_text(prompt, max_length=128):
    """
    Generate text based on the given prompt.

    Args:
        prompt (str): The input text prompt.
        max_length (int): The maximum length of the generated text.

    Returns:
        str: The generated text.
    """
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)