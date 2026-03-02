from loader import load_all_abilities, load_all_bugemons
from fight import Battle
from player import Player

def main():
    abilities = load_all_abilities("assets/json/attaques.json")
    bugemons  = load_all_bugemons("assets/json/bugemons.json", abilities)

    team_1 = [bugemons[0], bugemons[1], bugemons[2]]
    team_2 = [bugemons[3], bugemons[4], bugemons[5]]
    player_1 = Player(team_1)
    player_2 = Player(team_2)

    test_battle = Battle(player_1, player_2)
    test_battle.run_battle()

    for line in test_battle.log:
        print(line)
        
if __name__ == "__main__":
    main()