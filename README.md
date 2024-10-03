# Self-Learning AI Framework

A self-learning AI framework designed to dynamically modify its own code, create multiple agents, develop new tools, and build new AI frameworks. This project leverages OpenAI's API for natural language processing and code execution capabilities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Dynamic Code Modification**: The framework can modify existing code snippets based on user requests.
- **Multiple Agents**: Create and manage multiple AI agents for various tasks.
- **Tool Creation**: Dynamically generate new tools as required.
- **Custom AI Frameworks**: Build new AI frameworks tailored to specific needs.

## Installation

1. Clone the repository:
   ```bash

   git clone https://github.com/doulatdutta/self_learning_ai_framework.git
   ```
2. Mode to folder
   ```bash
   cd self_learning_ai_framework
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
4. Activate virtual environment
   ```bash
   source venv/bin/activate
   
* On Windows use 
   ```bash
   venv\Scripts\activate
   ``` 
* On Windows use If you encounter an error regarding execution policies, you can temporarily bypass it by running:
   ```bash
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   ```
6. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
7. Rename example.env file in the config folder as .env
   
   add your OpenAI API key:
   
   `API_KEY=your_openai_api_key`
   
   `DB_PASSWORD=your_database_password`
   

8. To start the framework, run the main.py file:
   ```bash
   python main.py
   ```


## Usage

You can interact with the AI by typing commands in the terminal. Some example commands:

`Modify Code`: Type modify code add print statement to add a print statement to the code.

`Ask Questions`: Simply type your question or request, and the AI will respond.

`List Code Files`: Type list code files to view all code files in the project.

`Create Framework`: Type create framework <name> to generate a new AI framework.

`read code` : when entered, reads the code files from the specified `CODE_FOLDER` and prints their contents

`generate code for <task>` : the AI retrieves the learned code and provides a complete snippet based on the specified task.read

`analyze stock market for tomorrow` he program will run the stock prediction process

To exit, type `exit` or `quit`.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## The self_learning_ai_framework you're building is quite advanced and includes a variety of powerful features. Here's a breakdown of its key features and capabilities:

**1. Self-Learning & Code Modification :**

`Code Reading and Suggestion`: The framework reads all the code files from the specified folder (CODE_FOLDER) and can provide feedback or suggestions on where and what to edit. This helps in creating a system that actively assists in improving its own codebase based on requirements.

`Code Executor`: It executes code dynamically and allows the AI to modify the code itself as per the user's instructions.
Code Modifier: This component is responsible for making changes to the code, enabling the framework to adjust and optimize the code as needed based on user input.

**2. Framework Creation and Management :**

`Framework Creation`: Users can create new frameworks using commands like create framework <name>. This feature helps expand the system with new components and tools as needed.

`Framework Listing:` You can list all the frameworks created and available within the system using the list frameworks command.

**3. AI Interaction and Learning :**

`Natural Language Interaction`: The framework integrates with OpenAI's API (gpt-3.5-turbo), allowing users to communicate with the AI through natural language. The AI can respond to queries, provide suggestions, and assist in decision-making regarding code, frameworks, and more.

`PDF Processing and Model Training`: The framework can read PDF files (e.g., training materials) and use the content to train models. This feature allows it to learn from structured data or reference documents.

`Model Training and Management:` The framework supports model training based on provided content and stores models for later use.

**4. Automation and Installation of Packages :**

`Package Auto-Installation`: The framework can automatically install necessary Python packages by executing terminal commands (e.g., pip install). It checks whether a package is installed and proceeds with the installation if necessary, all controlled by user prompts.

`Terminal Command Execution`: The system can execute terminal commands and provide the result or errors if any occur. This makes it capable of automating tasks, such as package installation or executing other system commands.

**5. Logging and Debugging :**

`Logging System`: The framework uses a logging mechanism to keep track of activities and processes within the system. It logs significant events, such as when the AI is started, framework creation, and user interactions.

`Debug Mode`: The system includes a debug mode that logs more detailed information for troubleshooting and improving the framework during development.

**6. File Management and Browsing :**

`Recursive File Browsing`: It can browse and read code files recursively from the main folder and its subfolders. This enables the AI to access and process all the files in the project directory, ensuring a comprehensive understanding of the entire codebase.

`Code Display`: The system can display the contents of files to the user, making it easier to view and understand the structure of the code.

**7. API Key Management :**

`Secrets Management`: The framework has a secrets management system that stores sensitive information like API keys securely. This allows the framework to interface with external services (e.g., OpenAI) while keeping sensitive data safe.

**8. Dynamic Task Management :**

`Agent Management`: The framework is capable of spawning additional agents to handle specific tasks. For complex scenarios, it can create multiple agents to break down and execute tasks efficiently.

`Tool Management`: The framework can check if required tools are installed and handle installations as needed, ensuring that all dependencies are met for successful operation.

**9. AI Learning and Autonomous Operation :**

`Self-Improvement`: The core idea of this framework is to be self-learning, meaning it can autonomously evolve by suggesting improvements to its own code, creating new frameworks or tools, and managing its resources based on requirements.

`Autonomous Agent Spawning`: Based on tasks or goals provided by the user, the framework can autonomously create new agents or modify existing agents to execute tasks like data analysis, graph interpretation, and more.


## Future Potential:

**Fully Autonomous `AI Agent`:** With further enhancements, the framework could operate as a fully autonomous AI agent, capable of not only analyzing code and suggesting improvements but also executing changes and learning from its environment.

**Self-Creating Tools and Frameworks:** The framework could eventually build its own tools and frameworks as necessary to accomplish tasks efficiently without user intervention.
These features make the `self_learning_ai_framework` highly versatile and capable of automating development processes, improving itself, and managing complex projects with minimal intervention.
