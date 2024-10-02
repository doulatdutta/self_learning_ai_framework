from .agent_base import AgentBase

class WorkerAgent(AgentBase):
    def __init__(self, agent_id, name, task_queue):
        """
        Worker agent responsible for performing tasks.

        :param agent_id: Unique identifier for the agent
        :param name: Name of the agent
        :param task_queue: Queue of tasks assigned to the agent
        """
        super().__init__(agent_id, name)
        self.task_queue = task_queue

    def execute_task(self, task):
        """
        Executes a given task.
        """
        print(f"Worker Agent {self.name} is executing task: {task}")
        # Perform the task (dummy implementation for now)
        # In a real implementation, the task logic goes here
        self.task_queue.remove(task)
        print(f"Worker Agent {self.name} has completed task: {task}")

    def process_tasks(self):
        """
        Processes all tasks in the queue.
        """
        while self.task_queue and self.status == "working":
            task = self.task_queue[0]
            self.execute_task(task)

    def add_task(self, task):
        """
        Adds a new task to the task queue.
        """
        self.task_queue.append(task)
        print(f"Task {task} added to Worker Agent {self.name}'s queue.")
