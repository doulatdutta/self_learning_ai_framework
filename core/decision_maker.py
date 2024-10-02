class DecisionMaker:
    def __init__(self):
        """
        DecisionMaker is responsible for making high-level decisions for the AI framework.
        """
        self.strategy = None

    def set_strategy(self, strategy):
        """
        Sets the decision-making strategy.

        :param strategy: A strategy for decision making (could be reinforcement learning, rule-based, etc.).
        """
        self.strategy = strategy

    def decide(self, environment_state):
        """
        Makes a decision based on the current state of the environment.

        :param environment_state: The current state of the environment.
        :return: A decision on the next action (e.g., generate new agent, modify code).
        """
        if self.strategy is None:
            raise Exception("No decision-making strategy set.")
        
        decision = self.strategy.make_decision(environment_state)
        print(f"Decision made: {decision}")
        return decision
