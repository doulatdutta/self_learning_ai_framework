class SelfAssessment:
    def __init__(self):
        """
        SelfAssessment is responsible for evaluating the framework's performance.
        """
        self.assessment_criteria = {}

    def set_criteria(self, criteria):
        """
        Sets the criteria for self-assessment.

        :param criteria: A dictionary of assessment criteria.
        """
        self.assessment_criteria = criteria

    def assess(self, agent, environment):
        """
        Assesses the agent's performance based on the current state of the environment.

        :param agent: The agent to assess.
        :param environment: The environment in which the agent is operating.
        :return: A report on the assessment.
        """
        performance = environment.assess_performance(agent)
        report = f"Agent {agent.name} performance: {performance}"

        # Compare against assessment criteria
        for criterion, threshold in self.assessment_criteria.items():
            if criterion in environment.get_state():
                value = environment.get_state()[criterion]
                report += f"\n{criterion}: {value} (threshold: {threshold})"
                if value < threshold:
                    report += " [Needs Improvement]"
                else:
                    report += " [Good]"

        print("Self-assessment complete.")
        return report
