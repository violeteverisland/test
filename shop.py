# shop.py
def display_shop_menu(character):  # 添加 character 参数
    print("\nWelcome to the Shop!")
    print("1. Buy Attack Boost (+5 Attack Power) - 50 gold")
    print("2. Buy Health Potion (+20 Health) - 30 gold")
    print("3. Buy Experience Potion (+20 Exp) - 40 gold")
    print("4. Exit Shop")
    print(f"Your current gold: {character.gold}")  # 使用 character 参数
    choice = input("Enter your choice: ")
    return choice

def buy_attack_boost(character):
    if character.gold >= 50:
        character.gold -= 50
        character.attack_power += 5
        print("You bought an Attack Boost! Attack Power increased by 5.")
    else:
        print("Not enough gold!")

def buy_health_potion(character):
    if character.gold >= 30:
        character.gold -= 30
        character.health += 20
        print("You bought a Health Potion! Health increased by 20.")
    else:
        print("Not enough gold!")

def buy_experience_potion(character):
    if character.gold >= 40:
        character.gold -= 40
        character.exp += 20
        print("You bought an Experience Potion! Gained 20 Exp.")
    else:
        print("Not enough gold!")

def visit_shop(character):  # 确保传递 character 参数
    while True:
        choice = display_shop_menu(character)  # 传递 character 参数
        if choice == "1":
            buy_attack_boost(character)
        elif choice == "2":
            buy_health_potion(character)
        elif choice == "3":
            buy_experience_potion(character)
        elif choice == "4":
            print("Exiting shop. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")