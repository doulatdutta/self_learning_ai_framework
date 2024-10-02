import subprocess

class CodeExecutor:
    def execute_code(self, code):
        try:
            exec(code)
        except Exception as e:
            return f"Error during execution: {str(e)}"

    def run_terminal_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}"
        except Exception as e:
            return f"Error while running command: {str(e)}"
