# import json
# from llama_cpp import Llama
from vllm import LLM, SamplingParams 
from huggingface_hub import snapshot_download

# Download the Phi-3 model locally (this will take time)
model_path = snapshot_download(
    repo_id="microsoft/phi-3-mini-4k-instruct",
    cache_dir="./models"
)

print(f"Model downloaded to: {model_path}")

# Load the model with vLLM
llm = LLM(model=model_path, dtype="float16")  # Use GPU acceleration if available

# Define input prompt
prompt = "What is the capital of France?"

# Set sampling parameters
sampling_params = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=100)

# Generate response
output = llm.generate(prompt, sampling_params)

# Print response
print("Response:", output[0].outputs[0].text)
