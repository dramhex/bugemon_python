from loader import load_all_abilities, load_all_bugemons
from fight import run_turn

def main():
    abilities = load_all_abilities("assets/json/attaques.json")
    bugemons  = load_all_bugemons("assets/json/bugemons.json", abilities)

    log = []
    
    log.extend(run_turn(bugemons[0], bugemons[1], abilities["fouet_liane"], abilities["spore_collante"]))
    
    for line in log:
        print(line)
        
if __name__ == "__main__":
    main()