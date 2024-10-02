class ToolBase:
    def __init__(self, tool_id, name, description):
        """
        Base class for all tools.
        
        :param tool_id: Unique identifier for the tool.
        :param name: Name of the tool.
        :param description: Brief description of the tool's purpose.
        """
        self.tool_id = tool_id
        self.name = name
        self.description = description

    def execute(self, *args, **kwargs):
        """
        Executes the tool's main functionality. Must be overridden by subclasses.
        
        :param args: Positional arguments for tool execution.
        :param kwargs: Keyword arguments for tool execution.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

    def get_info(self):
        """
        Returns the basic information of the tool.
        
        :return: Tool information as a dictionary.
        """
        return {
            "tool_id": self.tool_id,
            "name": self.name,
            "description": self.description
        }
