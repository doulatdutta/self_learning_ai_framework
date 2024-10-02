import os
import subprocess
from core.pdf_reader import PDFReader
from config.secrets import Secrets

class Colors:
    RED = "\033[91m"  # Red text
    GREEN = "\033[92m"  # Green text
    BLUE = "\033[94m"   # Blue text
    RESET = "\033[0m"   # Reset to default color

class AgentManager:
    def __init__(self):
        self.secrets = Secrets()
        self.pdf_reader = PDFReader()

    def run_agent(self, agent_type, *args):
        if agent_type == "install_tool":
            tool_name = args[0]
            self.install_tool(tool_name)
        elif agent_type == "train_with_pdf":
            input_folder = args[0]
            self.train_with_pdf(input_folder)
        else:
            print("Unknown agent type.")

    def install_tool(self, tool_name):
        if self.check_tool_installed(tool_name):
            print(f"{Colors.GREEN}{tool_name} is already installed.{Colors.RESET}")
        else:
            print(f"Installing {tool_name}...")
            command = f"pip install {tool_name}"
            self.run_terminal_command(command)

    def check_tool_installed(self, tool_name):
        result = subprocess.run(["pip", "show", tool_name], capture_output=True, text=True)
        return result.returncode == 0  # True if installed

    def run_terminal_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f"{Colors.RED}Error: {result.stderr}{Colors.RESET}")
        except Exception as e:
            print(f"Error while running command: {str(e)}")

    def train_with_pdf(self, input_folder):
        for file in os.listdir(input_folder):
            if file.endswith('.pdf'):
                pdf_path = os.path.join(input_folder, file)
                print(f"Reading PDF file: {pdf_path}")
                text = self.pdf_reader.read_pdf(pdf_path)
                # Implement your model training logic here
                print(f"Training with text from {file} completed.")

