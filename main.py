import json
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

# Download the model file
model_path = hf_hub_download(
    repo_id="lmstudio-community/Phi-3.1-mini-4k-instruct-GGUF",
    filename="Phi-3.1-mini-4k-instruct-IQ3_M.gguf",
    cache_dir="./models"  # Change path if needed
)

# Load config from JSON
with open("model_config.json", "r") as file:
    config = json.load(file)

# Extract parameters
load_params = config["load_params"]
inference_params = config["inference_params"]

# Initialize model with load_params
llm = Llama(
    model_path=model_path,
    n_ctx=load_params.get("n_ctx", 2048),
    n_batch=load_params.get("n_batch", 512),
    n_gpu_layers=load_params.get("n_gpu_layers", 20),
    use_mlock=load_params.get("use_mlock", True),
    main_gpu=load_params.get("main_gpu", 0),
    tensor_split=load_params.get("tensor_split", [0]),
    seed=load_params.get("seed", -1),
    f16_kv=load_params.get("f16_kv", True),
    use_mmap=load_params.get("use_mmap", True),
    no_kv_offload=load_params.get("no_kv_offload", False),
)

# Generate a chat response using inference parameters
response = llm.create_chat_completion(
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
    temperature=inference_params.get("temp", 0.8),
    top_p=inference_params.get("top_p", 0.95),
    top_k=inference_params.get("top_k", 40),
    repeat_penalty=inference_params.get("repeat_penalty", 1.1),
    max_tokens=inference_params.get("n_predict", -1),
)

# Print the response
print(response["choices"][0]["message"]["content"])
