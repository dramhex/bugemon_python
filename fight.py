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

def apply_effect(launcher: Bugemon, target: Bugemon, effects: list) -> list[str]:
    log = []
    
    if effects:
        if effects["cible"] == "lanceur":
            if effects["type"] == "soin":  
                launcher.health.apply_modifier(effects["modificateur"])
                log.append(f"{launcher.name} a été soigné de {effects['modificateur']} PV")
            else:
                stat = getattr(launcher, effects["stat"])  # retourne launcher.defense, launcher.initiative, etc.
                stat.apply_modifier(effects["modificateur"])
                
                if effects["modificateur"] > 0:
                    log.append(f"{effects['stat']} de {launcher.name} augmente de {effects['modificateur']}".capitalize())
                else:
                    log.append(f"{effects['stat']} de {launcher.name} diminue de {effects['modificateur']}".capitalize())
                    
        elif effects["cible"] == "equipe":
                pass # implémenter une boucle qui soigne toute l'équipe
        else:
            if target.is_alive:
                stat = getattr(target, effects["stat"])  
                stat.apply_modifier(effects["modificateur"])
                
                if effects["modificateur"] > 0:
                    log.append(f"{effects['stat']} de {target.name} augmente de {effects['modificateur']}".capitalize())
                else:
                    log.append(f"{effects['stat']} de {target.name} diminue de {effects['modificateur']}".capitalize())
    return log

def get_priority(bugemon_1: Bugemon, bugemon_2: Bugemon, ability_1, ability_2) -> tuple[Bugemon, Bugemon, Ability, Ability]:
    if bugemon_1.initiative.current_value >= bugemon_2.initiative.current_value:
        first, second = bugemon_1, bugemon_2
        first_ability, second_ability = ability_1, ability_2
    else:
        first, second = bugemon_2, bugemon_1
        first_ability, second_ability = ability_2, ability_1
    return first, second, first_ability, second_ability

def use_ability(launcher: Bugemon, target: Bugemon, ability: Ability) -> list[str]:
    log = []
    
    damage = calculate_damage(launcher, target, ability)
    target.health.apply_modifier(-damage)
    log.append(f"{launcher.name} utilise {ability.name} !")
    log.append(f"{target.name} perd {damage} PV !")
    log.extend(apply_effect(launcher, target, ability.effects))

    if not target.is_alive:
        log.append(f"{target.name} est K.O. !")
    
    return log

def run_turn(bugemon_1: Bugemon, bugemon_2: Bugemon, ability_1: Ability, ability_2: Ability) -> list[str]:
    log = []
    
    first, second, first_ability, second_ability = get_priority(bugemon_1, bugemon_2, ability_1, ability_2)
    
    log.extend(use_ability(first, second, first_ability))
    
    if second.is_alive:
        log.extend(use_ability(second, first, second_ability))
    
    return log

def run_battle(player: Bugemon, enemy: Bugemon) -> list[str]:
    pass