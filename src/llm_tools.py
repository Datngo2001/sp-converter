
def create_cs_file(file_name: str, content: str) -> None:
    """
    Create a C# file with the given name and content.
    """
    with open(file_name, 'w') as file:
        file.write(content)