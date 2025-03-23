from CharacterLibary import Character
from CharacterLibary import Enemy
import json
#filename is for character "CharacterList.json" and enemy is "enemyList.json"

GameState = True
while GameState is True: 
    print("Character and enemy maker initialized.")
    selection = input(f"Select Character or Enemy.\n")
    if selection == "Character":
        print("Selected Character")
        name = input("character's name\n")
        hp = input("hp amount\n")
        atk = input("attack stat\n")
        rarity = input("character rarity\n")
        saved_character= Character(name,hp,atk,rarity)
        print(f"{saved_character.name}, {saved_character.hp}, {saved_character.atk}, {saved_character.rarity}")
        match int(input("Procced to save Character?\n 1: yes, 2: no\n")):
            case 1:
                Character.Save_Character(saved_character)
            case _:
                break
    elif selection =="Enemy":
        print("Selected Enemy")
        name = input("enemy's name\n")
        hp = input("hp amount\n")
        atk = input("atk amount\n")
        print("Choose the elemental type: Normal, Fairty, Ghost\n")
        match int(input("1 = Normal, 2 = Fairy, 3 = Ghost\n")):
            case 1: 
                Enemy_type = ("Normal")
            case 2:
                Enemy_type = ("Fairy")
            case 3:
                Enemy_type = ("Ghost")
            case _:
                print("Invalid option!")
                break
        saved_enemy= Enemy(name,hp,atk,Enemy_type)
        print(f"{saved_enemy.name}, {saved_enemy.hp}, {saved_enemy.atk}, {saved_enemy.etype}")
        match int(input("procceed to save enemy?\n 1 = yes, 2 = no\n")):
            case 1:
                Enemy.Save_Enemy(saved_enemy)
            case _:    
                break
    else:
        print(f"Not an avilable option, please select Character or Enemy.\n *your input is case sensitive*")
        break