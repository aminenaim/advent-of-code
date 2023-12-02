import os

def get_file_name() -> str:
    # Check if the CONTEXT environment variable is set
    demo_env = os.environ.get('CONTEXT', 'demo').lower()

    # Return the corresponding file name
    if demo_env == 'demo':
        return 'demo-input.txt'
    else:
        return 'input.txt'

def get_input() -> list[str]:
    file_name = get_file_name()
    print(f"loading {file_name}")

    # reading lines and returning them as a list of lines
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print(f"error: file {file_name} not found.")
        return None
