from bugemon_stat import Stat
from ability import Ability

class Bugemon:
    def __init__(self, identifier: str, name: str , elementary_type: str, health: int, attack: int, defense: int, initiative: int, ability_set: list[Ability], starter: bool, level: int = 1):
        self.identifier = identifier
        self.name = name
        self.elementary_type = elementary_type
        self.health = Stat(health) # toutes les stats ont la meme logique finalement
        self.attack = Stat(attack)
        self.defense = Stat(defense)
        self.initiative = Stat(initiative)
        self.ability_set = ability_set
        self.level = level
        self.starter = starter
        self.experience = 0
        
    @property
    def is_alive(self):
        return self.health.current_value > 0

    def reset_stats(self):
        self.attack.reset_current_value()
        self.defense.reset_current_value()
        self.initiative.reset_current_value()
    