import os
import sys
from dotenv import load_dotenv
import openai

# Set the path to the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import Settings after modifying sys.path
from config.settings import Settings

# Load environment variables from .env file
load_dotenv()

# Function to read code files from the specified directory
def read_code_from_folder(code_folder):
    code_files = {}
    for dirpath, dirnames, filenames in os.walk(code_folder):
        # Remove the venv folder from the search
        if 'venv' in dirnames:
            dirnames.remove('venv')
        for file in filenames:
            if file.endswith('.py'):  # Read only Python files; Add more extensions if needed
                file_path = os.path.join(dirpath, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    code_files[file_path] = f.read()
    return code_files

# Function to modify code based on user request
def modify_code_with_openai(user_request, existing_code):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Here is the code:\n{existing_code}\n\nUser request: {user_request}"}
            ]
        )
        modified_code = response.choices[0].message['content']
        return modified_code
    except Exception as e:
        print(f"Error modifying code: {e}")
        return None

# Main function
def main():
    # Load settings
    settings = Settings()

    # Load OpenAI API key from environment variable
    openai.api_key = os.getenv('API_KEY')

    # Get code folder from settings
    code_folder = settings.get('code_folder')
    if code_folder is None:
        print("Error: Code folder path is not set in settings.")
        return

    print(f"Using code folder: {code_folder}")

    # Read code from the folder
    code_files = read_code_from_folder(code_folder)

    # Prompt user for code modification request
    user_request = input("What modification would you like to make to the code? ")

    # Process each code file and modify
    for file_path, existing_code in code_files.items():
        print(f"Modifying {file_path}...")
        modified_code = modify_code_with_openai(user_request, existing_code)
        if modified_code:
            # Save the modified code back to the file
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_code)
                print(f"Modified code written to {file_path}")
            except Exception as e:
                print(f"Error writing to {file_path}: {e}")
        else:
            print(f"Failed to modify {file_path}")

if __name__ == "__main__":
    main()
