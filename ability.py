class Ability:
    def __init__(self, identifier: str, name: str, description: str, elementary_type: str, power: int, effects: dict):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.elementary_type = elementary_type
        self.power = power
        self.effects = effects