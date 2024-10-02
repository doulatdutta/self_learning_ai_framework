# agents/agent.py

class Agent:
    def __init__(self):
        print("Agent initialized.")

    def perform_task(self, task):
        print(f"Performing task: {task}")

if __name__ == "__main__":
    agent = Agent()
    agent.perform_task("Example Task")
