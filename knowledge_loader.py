import os

class KnowledgeLoader:
    def __init__(self, base_file_path):
        self.base_file_path = base_file_path

    def load_file(self, file_path):
        complete_file_path = os.path.join(self.base_file_path, file_path)
        
        if not os.path.exists(complete_file_path):
            raise FileNotFoundError(f"The file {complete_file_path} does not exist.")
        
        with open(complete_file_path, 'r') as file:
            content = file.read()
        
        return content