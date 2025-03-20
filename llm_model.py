from vllm import LLM, SamplingParams 
from huggingface_hub import snapshot_download

class LLMModel:
    def __init__(self, repo_id, cache_dir, dtype="float16"):
        self.model_path = snapshot_download(repo_id=repo_id, cache_dir=cache_dir)
        print(f"Model downloaded to: {self.model_path}")
        self.llm = LLM(model=self.model_path, dtype=dtype)
    
    def generate_response(self, prompt, temperature=0.7, top_p=0.9, max_tokens=100):
        sampling_params = SamplingParams(temperature=temperature, top_p=top_p, max_tokens=max_tokens)
        output = self.llm.generate(prompt, sampling_params)
        return output[0].outputs[0].text