from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="lmstudio-community/Phi-3.1-mini-4k-instruct-GGUF",
	filename="Phi-3.1-mini-4k-instruct-IQ3_M.gguf",
)

llm.create_chat_completion(
	messages = [
		{
			"role": "user",
			"content": "What is the capital of France?"
		}
	]
)