import random

from bugemon import Bugemon
from ability import Ability

TYPE_CHART = {
    ("Flora", "Aqua"): 1.5,
    ("Aqua", "Pyro"): 1.5,
    ("Pyro", "Litho"): 1.5,
    ("Litho", "Flora"): 1.5,
    ("Aqua", "Flora"): 0.75, 
    ("Pyro", "Aqua"): 0.75,
    ("Litho", "Pyro"): 0.75,
    ("Flora", "Litho"): 0.75
}

def calculate_damage(launcher: Bugemon, target: Bugemon, ability: Ability) -> int:
    attack_factor = (100 + launcher.attack.current_value) / 100
    defense_factor = 100 / (100 + target.defense.current_value)
    
    type_multiplier = calculate_type_multiplier(ability.elementary_type, target.elementary_type)
    critical_multiplier = calculate_critical_multiplier()
    
    damage = int(ability.power * attack_factor * defense_factor * type_multiplier * critical_multiplier)
    return damage

def calculate_type_multiplier(ability_elementary_type: str, target_elementary_type: str) -> float:
    return TYPE_CHART.get((ability_elementary_type, target_elementary_type), 1) #si c'est pas dans le tableau c'est x1

def calculate_critical_multiplier() -> float:
    return 1.5 if random.random() < 0.1 else 1 #10% de chances de faire un coup critique (x1.5)

def apply_effect(launcher: Bugemon, target: Bugemon, ability: Ability):
    pass

def use_ability(launcher: Bugemon, target: Bugemon, ability: Ability):
    damage = calculate_damage(launcher, target, ability)
    target.health.apply_modifier(-damage)
    
    effects = ability.effects
    if effects:
        if effects["cible"] == "lanceur":
            if effects["type"] == "soin":  
                launcher.health.apply_modifier(effects["modificateur"])
            else:
                stat = getattr(launcher, effects["stat"])  # retourne launcher.defense, launcher.initiative, etc.
                stat.apply_modifier(effects["modificateur"])
        elif effects["cible"] == "equipe":
                pass # implémenter une boucle qui soigne toute l'équipe
        else:
            if target.is_alive:
                stat = getattr(target, effects["stat"])  
                stat.apply_modifier(effects["modificateur"])
                
    
    
    