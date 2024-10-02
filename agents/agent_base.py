class AgentBase:
    def __init__(self, agent_id, name):
        """
        Base class for all agents.

        :param agent_id: Unique identifier for the agent
        :param name: Name of the agent
        """
        self.agent_id = agent_id
        self.name = name
        self.status = "idle"  # can be idle, working, or stopped

    def start(self):
        """
        Starts the agent.
        """
        self.status = "working"
        print(f"Agent {self.name} with ID {self.agent_id} started.")

    def stop(self):
        """
        Stops the agent.
        """
        self.status = "stopped"
        print(f"Agent {self.name} with ID {self.agent_id} stopped.")

    def get_status(self):
        """
        Returns the current status of the agent.
        """
        return self.status

    def execute_task(self, task):
        """
        Placeholder for task execution. Subclasses should override this method.
        """
        raise NotImplementedError("Subclasses must implement this method.")
