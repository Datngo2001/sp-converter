from llm_model import LLMModel

if __name__ == "__main__":
    # Initialize the model
    model = LLMModel(repo_id="microsoft/phi-3-mini-4k-instruct", cache_dir="./models")
    
    # Define input prompt
    prompt = "What is the capital of France?"
    
    # Generate and print response
    response = model.generate_response(prompt)
    print("Response:", response)