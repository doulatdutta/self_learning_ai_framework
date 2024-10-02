import os

class CodeModifier:
    def modify_code(self, original_code, modification):
        try:
            # Logic to modify code
            new_code = original_code.replace("old_function", modification)
            return new_code
        except Exception as e:
            return f"Error while modifying code: {str(e)}"

    def create_new_file(self, file_path, content):
        try:
            with open(file_path, 'w') as new_file:
                new_file.write(content)
            return f"File {file_path} created."
        except Exception as e:
            return f"Error while creating file: {str(e)}"
