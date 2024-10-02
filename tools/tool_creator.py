from .tool_base import ToolBase

class ToolCreator:
    def __init__(self):
        """
        ToolCreator is responsible for generating new tools dynamically.
        """
        self.tools = {}

    def create_tool(self, tool_id, name, description, functionality_code):
        """
        Dynamically creates a new tool and registers it.

        :param tool_id: Unique identifier for the new tool.
        :param name: Name of the tool.
        :param description: A brief description of the tool's purpose.
        :param functionality_code: A function that defines the tool's functionality.
        :return: The dynamically created tool instance.
        """
        # Create a new subclass of ToolBase dynamically
        class DynamicTool(ToolBase):
            def execute(self, *args, **kwargs):
                """
                Executes the functionality of the dynamically generated tool.
                """
                return functionality_code(*args, **kwargs)

        # Instantiate the new tool
        new_tool = DynamicTool(tool_id, name, description)
        self.tools[tool_id] = new_tool
        print(f"Tool {name} with ID {tool_id} has been created.")
        return new_tool

    def get_tool(self, tool_id):
        """
        Retrieves a tool by its ID.

        :param tool_id: The unique identifier of the tool.
        :return: The tool instance if it exists, or None if not found.
        """
        return self.tools.get(tool_id)

    def remove_tool(self, tool_id):
        """
        Removes a tool by its ID.

        :param tool_id: The unique identifier of the tool to remove.
        :return: None
        """
        if tool_id in self.tools:
            del self.tools[tool_id]
            print(f"Tool with ID {tool_id} has been removed.")
        else:
            print(f"Tool with ID {tool_id} not found.")


## New

# tools/tool_creator.py

class ToolCreator:
    def create_tool(self, tool_name):
        # This is a simplified example. You might want to use templates or more complex logic.
        tool_code = f"""
def {tool_name}():
    print('Executing {tool_name}...')
    # Add your tool logic here
"""
        return tool_code

