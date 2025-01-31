class ToolStateError(Exception):
    """Raise this error if the tool is in the wrong state to perform such a command."""
    pass


class ToolConfigurationError(Exception):
    """Raise this error if there is something wrong with how the tool is configured"""
    pass


class Tool:
    def __init__(self, index, name, **kwargs):
        self._machine = None  # This is set in Machine.py load_tool()
        if not isinstance(index, int) or not isinstance(name, str):
            raise ToolConfigurationError("Incorrect usage: load_tool(<tool_number>, <name>, **kwargs)")
        self.index = index
        self.name = name
        self.is_active_tool = False
        for k, v in kwargs.items():
            setattr(self, k, v)
            
            
    def post_load(self):
        """Run any code after tool has been associated with the machine."""
        pass
