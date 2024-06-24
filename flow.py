class Flow:
    def __init__(self):
        self.actions = {}

    def add_action(self, name, action):
        self.actions[name] = action

    def execute_action(self, name, *args, **kwargs):
        action = self.actions.get(name)
        if not action:
            raise ValueError(f"Action '{name}' not found in flow.")
        return action.execute(*args, **kwargs)