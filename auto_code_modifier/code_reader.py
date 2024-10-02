import os

class CodeReader:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def read_all_code(self):
        code_files = {}
        for dirpath, _, files in os.walk(self.root_folder):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(dirpath, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        code_files[file_path] = f.read()
        return code_files
