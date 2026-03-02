class Bugemon:
    def __init__(self, name , elementary_type : str, health, attack, defense, initiative, level = 1):
        self.name = name
        self.elementary_type = elementary_type
        self.health = health
        self.attack = attack
        self.defense = defense
        self.initiative = initiative
        self.level = level
        self.experience = 0