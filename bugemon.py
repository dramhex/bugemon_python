from bugemon_stat import Stat

class Bugemon:
    def __init__(self, name , elementary_type, base_health, attack, defense, initiative, level = 1):
        self.name = name
        self.elementary_type = elementary_type
        self.base_health = base_health
        self.current_health = base_health
        self.attack = Stat(attack)
        self.defense = Stat(defense)
        self.initiative = Stat(initiative)
        self.level = level
        self.experience = 0