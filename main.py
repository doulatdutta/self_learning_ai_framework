import os
import subprocess
import logging
from core.code_executor import CodeExecutor
from core.code_modifier import CodeModifier
from config.secrets import Secrets
from frameworks import framework_creator
from models.model_manager import ModelManager
from core.pdf_reader import PDFReader
import openai
from datetime import datetime
from frameworks.framework_creator import FrameworkCreator
from config.settings import CODE_FOLDER


class Colors:
    GREEN = "\033[92m"  # Green text
    BLUE = "\033[94m"   # Blue text
    RED = "\033[91m"    # Red text
    RESET = "\033[0m"   # Reset to default color


def process_input(user_input, secrets, code_files):
    api_key = secrets.get_secret("api_key")
    openai.api_key = api_key

    if user_input.lower() == "read the code from my project":
        return "\n".join([f"Read from {path}:\n{code}" for path, code in code_files.items()])

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        reply = response.choices[0].message['content']
        return reply
    except Exception as e:
        return f"Error: {str(e)}"


def run_terminal_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Error while running command: {str(e)}"


def auto_install_package(package_name):
    command = f"pip install {package_name}"
    result = run_terminal_command(command)
    if "Successfully installed" in result or "Requirement already satisfied" in result:
        print(f"{Colors.GREEN}Successfully installed {package_name}.{Colors.RESET}")
    else:
        print(f"{Colors.RED}Failed to install {package_name}: {result}{Colors.RESET}")


def process_pdf_files(input_folder, model_manager):
    pdf_reader = PDFReader()
    for file in os.listdir(input_folder):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, file)
            print(f"Reading PDF file: {pdf_path}")
            text = pdf_reader.read_pdf(pdf_path)

            model_name = "MyModel"
            model_manager.train_model(model_name, text)


def browse_code_in_folder(folder_path):
    """Recursively reads all Python files in a given folder and its subfolders."""
    code_files = {}
    for dirpath, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):  # Adjust this if you want other file types
                file_path = os.path.join(dirpath, file)
                try:
                    with open(file_path, 'r') as f:
                        code_content = f.read()
                    code_files[file_path] = code_content
                except Exception as e:
                    print(f"{Colors.RED}Error reading file {file_path}: {e}{Colors.RESET}")
    return code_files


def main():
    logger = logging.getLogger('app_logger')
    logger.info("Application started.")
    secrets = Secrets()
    code_executor = CodeExecutor()
    code_modifier = CodeModifier()
    model_manager = ModelManager()

    input_folder = "input"

    # Check if there are PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    if pdf_files:
        train_choice = input("Would you like to train with PDF files? (yes/no): ")
        if train_choice.lower() == 'yes':
            print("Starting training with PDF files...")
            process_pdf_files(input_folder, model_manager)
            print(f"{Colors.GREEN}Training completed.{Colors.RESET}")
        else:
            print(f"{Colors.BLUE}Training skipped. You can now interact with the AI.{Colors.RESET}")
    else:
        print(f"{Colors.RED}No PDF files found in the input folder. You can now interact with the AI.{Colors.RESET}")

    # Use CODE_FOLDER to read code files
    code_folder_path = CODE_FOLDER
    print(f"Reading code files from: {code_folder_path}")

    code_files = browse_code_in_folder(code_folder_path)

    while True:
        user_input = input(f"{Colors.BLUE}You: {Colors.RESET}")
        if user_input.lower() in ['exit', 'quit']:
            logger.info("Exiting the application.")
            break

        if user_input.lower() == "list code files":
            if code_files:
                print(f"{Colors.GREEN}Code files found:{Colors.RESET}")
                for path in code_files.keys():
                    print(f"{Colors.BLUE}{path}{Colors.RESET}")
            else:
                print(f"{Colors.RED}No code files found in the specified folder.{Colors.RESET}")

        elif user_input.lower().startswith("create framework"):
            framework_name = user_input.split("create framework ")[1]
            framework_creator.create_framework(framework_name)
        elif user_input.lower() == "list frameworks":
            frameworks = framework_creator.list_frameworks()
            if frameworks:
                print(f"{Colors.GREEN}Available frameworks: {', '.join(frameworks)}{Colors.RESET}")
            else:
                print(f"{Colors.RED}No frameworks available.{Colors.RESET}")

        elif "install" in user_input.lower():
            package_name = user_input.split("install ")[1]
            auto_install_package(package_name)
        else:
            response = process_input(user_input, secrets, code_files)
            print(f"{Colors.GREEN}AI: {response}{Colors.RESET}")


if __name__ == "__main__":
    main()
