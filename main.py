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
from agents.news_scraper_agent import NewsScraperAgent
from agents.financial_analyzer_agent import FinancialAnalyzerAgent
from agents.technical_analysis_agent import TechnicalAnalysisAgent

class Colors:
    GREEN = "\033[92m"  # Green text
    BLUE = "\033[94m"   # Blue text
    RED = "\033[91m"    # Red text
    RESET = "\033[0m"   # Reset to default color

class CodeLearner:
    def __init__(self):
        self.code_structure = {}

    def learn_code(self, code_files):
        """Learns the structure of the provided code files."""
        for file_path, code in code_files.items():
            self.code_structure[file_path] = code

    def generate_code(self, task_description):
        """Generates code based on the learned structure and the task description."""
        # A simple example; integrate more sophisticated logic for real use
        generated_code = f"# Generated code for task: {task_description}\n"
        for file_path, code in self.code_structure.items():
            generated_code += f"\n# From {file_path}\n{code}\n"
        return generated_code

def process_input(user_input, secrets):
    api_key = secrets.get_secret("api_key")
    openai.api_key = api_key
    
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
            if file.endswith('.py'):
                file_path = os.path.join(dirpath, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_files[file_path] = f.read()
                except UnicodeDecodeError:
                    # Try with a different encoding if utf-8 fails
                    try:
                        with open(file_path, 'r', encoding='ISO-8859-1') as f:
                            code_files[file_path] = f.read()
                    except UnicodeDecodeError:
                        print(f"Could not decode {file_path} with utf-8 or ISO-8859-1. Skipping this file.")
                    except Exception as e:
                        print(f"Error reading {file_path}: {str(e)}")
                except Exception as e:
                    print(f"Error reading {file_path}: {str(e)}")
    return code_files


class StockPredictionCoordinator:
    def __init__(self):
        self.news_scraper = NewsScraperAgent()
        self.financial_analyzer = FinancialAnalyzerAgent()
        self.technical_analyzer = TechnicalAnalysisAgent()

    def find_top_stocks(self):
        # Step 1: Get top 20 companies from news
        companies_from_news = self.news_scraper.get_top_news_related_companies()

        # Step 2: Analyze financial data and filter to 10 companies
        top_10_companies = self.financial_analyzer.analyze_and_filter(companies_from_news)

        # Step 3: Perform technical analysis on 10 companies
        final_suggestions = self.technical_analyzer.perform_technical_analysis(top_10_companies)

        return final_suggestions

def analyze_stock_market():
    # 1. Step 1: Find top news related to Indian stock market
    print(f"{Colors.BLUE}Step 1: Finding top news related to Indian stock market...{Colors.RESET}")
    news_agent = NewsScraperAgent()
    top_20_companies = news_agent.get_top_20_companies()
    
    if not top_20_companies:
        print(f"{Colors.RED}Error fetching top companies based on news.{Colors.RESET}")
        return
    
    print(f"{Colors.GREEN}Top 20 companies suggested by news: {top_20_companies}{Colors.RESET}")

    # 2. Step 2: Analyze financial data to filter down to top 10 companies
    print(f"{Colors.BLUE}Step 2: Analyzing financial data...{Colors.RESET}")
    financial_analyzer = FinancialAnalyzerAgent()
    top_10_companies = financial_analyzer.analyze_financial_data(top_20_companies)
    
    if not top_10_companies:
        print(f"{Colors.RED}Error analyzing financial data.{Colors.RESET}")
        return
    
    print(f"{Colors.GREEN}Top 10 companies after financial analysis: {top_10_companies}{Colors.RESET}")

    # 3. Step 3: Perform technical analysis to suggest best companies to buy
    print(f"{Colors.BLUE}Step 3: Performing technical analysis...{Colors.RESET}")
    technical_analyzer = TechnicalAnalysisAgent()
    best_companies = technical_analyzer.perform_technical_analysis(top_10_companies)
    
    if not best_companies:
        print(f"{Colors.RED}Error during technical analysis.{Colors.RESET}")
        return
    
    print(f"{Colors.GREEN}Best companies to buy based on technical analysis: {best_companies}{Colors.RESET}")



def main():
    logger = logging.getLogger('app_logger')
    logger.info("Application started.")
    secrets = Secrets()
    code_executor = CodeExecutor()
    code_modifier = CodeModifier()
    model_manager = ModelManager()
    code_learner = CodeLearner()

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

    while True:
        user_input = input(f"{Colors.BLUE}You: {Colors.RESET}")
        if user_input.lower() in ['exit', 'quit']:
            logger.info("Exiting the application.")
            break

        elif user_input.lower() == "list code files":
            code_files = browse_code_in_folder(CODE_FOLDER)
            if code_files:
                print(f"{Colors.GREEN}Code files found:\n{Colors.RESET}{', '.join(code_files.keys())}")
            else:
                print(f"{Colors.RED}No code files found in the specified folder.{Colors.RESET}")

        elif user_input.lower().startswith("read code"):
            code_files = browse_code_in_folder(CODE_FOLDER)
            if code_files:
                code_learner.learn_code(code_files)
                print(f"{Colors.GREEN}Learned the code structure from the files.{Colors.RESET}")
            else:
                print(f"{Colors.RED}No code files found to read.{Colors.RESET}")

        elif user_input.lower().startswith("generate code for"):
            task_description = user_input.split("generate code for ")[1]
            generated_code = code_learner.generate_code(task_description)
            print(f"{Colors.GREEN}Generated Code:\n{Colors.RESET}{generated_code}")

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
            response = process_input(user_input, secrets)
            print(f"{Colors.GREEN}AI: {response}{Colors.RESET}")

        if user_input.lower() == "analyze stock market for tomorrow":
            analyze_stock_market()
        else:
            response = process_input(user_input, secrets)
            print(f"{Colors.GREEN}AI: {response}{Colors.RESET}")

if __name__ == "__main__":
    main()
