class Stat:
    def __init__(self, base_value):
        self.base_value = base_value
        self.current_value = base_value

    def reset_current_value(self):
        self.current_value = self.base_value

    def apply_modifier(self, modifier):
        self.current_value = max(0, self.current_value + modifier)