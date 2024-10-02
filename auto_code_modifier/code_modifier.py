import openai
import os

class CodeModifier:
    def __init__(self, api_key):
        openai.api_key = api_key

    def suggest_code_changes(self, code, user_request):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a smart code assistant."},
                    {"role": "user", "content": f"The following code is part of the project: {code}"},
                    {"role": "user", "content": f"I want to {user_request}. How can I modify the code to do this?"}
                ]
            )
            suggested_code = response.choices[0].message['content']
            return suggested_code
        except Exception as e:
            return f"Error: {str(e)}"

    def modify_code(self, file_path, new_code):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_code)
        print(f"Code updated successfully in {file_path}")
