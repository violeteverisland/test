# main.py
import json
import time
from shop import visit_shop  # 导入商店功能
import threading

class Character:
    def __init__(self, name, level=1, exp=0, health=100, attack_power=10, gold=0):
        self.name = name
        self.level = level
        self.exp = exp
        self.exp_to_next_level = 100
        self.health = health
        self.attack_power = attack_power
        self.gold = gold

    def level_up(self):
        self.level += 1
        self.exp_to_next_level += 50
        self.health += 20
        self.attack_power += 5
        print(f"{self.name} leveled up! Level: {self.level}, Health: {self.health}, Attack Power: {self.attack_power}")

    def gain_exp(self, exp):
        self.exp += exp
        print(f"{self.name} gained {exp} exp. Total exp: {self.exp}")
        while self.exp >= self.exp_to_next_level:
            self.exp -= self.exp_to_next_level
            self.level_up()

    def gain_gold(self, gold):
        self.gold += gold
        print(f"{self.name} gained {gold} gold. Total gold: {self.gold}")



def save_game(character, filename="savegame.json"):
    try:
        with open(filename, "r") as file:
            save_data = json.load(file)
    except FileNotFoundError:
        save_data = {}

    save_data[character.name] = {
        "level": character.level,
        "exp": character.exp,
        "health": character.health,
        "attack_power": character.attack_power,
        "gold": character.gold
    }

    with open(filename, "w") as file:
        json.dump(save_data, file, indent=4)
    print(f"Game saved to {filename}")



def load_game(name, filename="savegame.json"):
    try:
        with open(filename, "r") as file:
            save_data = json.load(file)
    except FileNotFoundError:
        print(f"No save file found at {filename}.")
        return None

    if name in save_data:
        character_data = save_data[name]
        character = Character(name,
                              level=character_data["level"],
                              exp=character_data["exp"],
                              health=character_data["health"],
                              attack_power=character_data["attack_power"],
                              gold=character_data["gold"])
        print(f"Game loaded for {name}.")
        return character
    else:
        print(f"No saved data found for {name}.")
        return None



def choose_character():
    print("\nCharacter Selection:")
    print("1. Load Saved Character")
    print("2. Create New Character")
    choice = input("Enter your choice: ")

    if choice == "1":
        # 列出所有已存在的角色
        try:
            with open("savegame.json", "r") as file:
                save_data = json.load(file)
            if save_data:
                print("\nAvailable Characters:")
                for name in save_data.keys():
                    print(f"- {name}")
                name = input("Enter the name of the character you want to load: ")
                return load_game(name)
            else:
                print("No saved characters found. Please create a new character.")
                return choose_character()
        except FileNotFoundError:
            print("No save file found. Please create a new character.")
            return choose_character()

    elif choice == "2":
        try:
            with open("savegame.json", "r") as file:
                save_data = json.load(file)
        except FileNotFoundError:
            save_data = {}

        name = input("Enter your character's name: ")
        if name in save_data:
            print(f"A character with the name '{name}' already exists. Please choose a different name.")
            return choose_character()
        else:
            character = Character(name)
            save_game(character)
            return character

    else:
        print("Invalid choice. Please try again.")
        return choose_character()



def auto_battle(character):
    print("Auto-battle started. Type 'exit' to stop.")
    running = True

    # 创建一个线程来处理自动战斗逻辑
    def battle_thread():
        nonlocal running
        while running:
            time.sleep(2)  # 每2秒进行一次战斗
            exp_gain = 10
            gold_gain = 5
            character.gain_exp(exp_gain)
            character.gain_gold(gold_gain)
            print(f"{character.name} fought a battle! Gained {exp_gain} exp and {gold_gain} gold.")

    # 启动战斗线程
    thread = threading.Thread(target=battle_thread)
    thread.start()

    # 玩家可以通过输入命令来控制战斗
    while running:
        command = input().strip().lower()
        if command == "exit":
            running = False
            print("Exiting auto-battle...")
        else:
            print("Unknown command. Type 'exit' to stop auto-battle.")

    # 等待战斗线程结束
    thread.join()

def display_character_status(character):
    print("\nCharacter Status:")
    print(f"Name: {character.name}")
    print(f"Level: {character.level}")
    print(f"Experience: {character.exp}/{character.exp_to_next_level}")
    print(f"Health: {character.health}")
    print(f"Attack Power: {character.attack_power}")
    print(f"Gold: {character.gold}")


def main():
    print("Welcome to the Idle Game!")
    character = choose_character()  # 每次启动时选择角色

    while True:
        print("\nMenu:")
        print("1. Start Auto-Battle")
        print("2. Visit Shop")
        print("3. View Character Status")
        print("4. Save Game")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            auto_battle(character)
        elif choice == "2":
            visit_shop(character)  # 调用商店功能
        elif choice == "3":
            display_character_status(character)
        elif choice == "4":
            save_game(character)  # 保存当前角色状态
        elif choice == "5":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()