class Environment:
    def __init__(self):
        """
        Environment represents the external world in which the agents operate.
        """
        self.state = {}

    def update_state(self, key, value):
        """
        Updates the environment state with new information.

        :param key: Key of the state variable.
        :param value: Value of the state variable.
        :return: None
        """
        self.state[key] = value

    def get_state(self):
        """
        Returns the current state of the environment.

        :return: The current state as a dictionary.
        """
        return self.state

    def assess_performance(self, agent):
        """
        Evaluates the performance of an agent within the environment.

        :param agent: The agent to assess.
        :return: A performance score (placeholder for now).
        """
        # Simplified logic for performance assessment
        return "Performance is good." if agent.get_status() == "working" else "Performance needs improvement."
