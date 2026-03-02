from loader import load_all_abilities, load_all_bugemons

def main():
    abilities = load_all_abilities("assets/json/attaques.json")
    bugemons  = load_all_bugemons("assets/json/bugemons.json", abilities)

    for bugemon in bugemons:
        print(bugemon)

if __name__ == "__main__":
    main()