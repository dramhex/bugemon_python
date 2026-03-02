import json

from bugemon import Bugemon
from ability import Ability

def load_bugemon(data: dict, abilities: dict[str, Ability]) -> Bugemon:    
    ability_set = []
    for ability_id in data["attaques"]:
        ability_set.append(abilities[ability_id])
    
    return Bugemon(    
        data["id"], 
        data["nom"], 
        data["type"], 
        data["stats"]["pv"], 
        data["stats"]["attaque"], 
        data["stats"]["defense"], 
        data["stats"]["initiative"],
        ability_set
    )
    
def load_all_bugemons(filepath: str, abilities: dict[str, Ability]) -> list[Bugemon]:
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return [load_bugemon(b, abilities) for b in data["bugemons"]]
    
def load_ability(data: dict) -> Ability:
    return Ability(
        data["id"],
        data["nom"],
        data["description"],
        data["type"],
        data["puissance"],
        data["effets"][0]
    )
    
def load_all_abilities(filepath: str) -> dict[str, Ability]:
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    abilities = {}
    for ability_data in data["attaques"]:
        ability = load_ability(ability_data)
        abilities[ability.identifier] = ability
    
    return abilities