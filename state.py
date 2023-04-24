class State:
    def __init__(self) -> None:
        self.commands = []


    def get_last_command(self):
        if len(self.commands) == 0:
            return None
        return self.commands.pop()


    def add_command(self, command):
        self.commands.append(command)