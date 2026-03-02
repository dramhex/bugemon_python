from bugemon import Bugemon

def load_bugemon(data: dict) -> Bugemon:
    return Bugemon(
        data["id"], 
        data["nom"], 
        data["type"], 
        data["stats"]["pv"], 
        data["stats"]["attaque"], 
        data["stats"]["defense"], 
        data["stats"]["initiative"],
        []
        )