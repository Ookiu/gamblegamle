from CharacterLibary import Character
from CharacterLibary import Enemy
from CharacterLibary import Actions
import json
#filename is "CharacterList.json" and "enemyList.json"

wolf = Enemy("wolf",2000,50)
Jax = Character("Jax",1000,100)
Saber = Character("Saber",2000,20)
Skull = Character("Skull",800,200)

Jax.assign_rarity(5)
Saber.assign_rarity(4)
Skull.assign_rarity(3)

Character.SaveCharacter(Jax,"CharacterList.json")
Character.SaveCharacter(Saber,"CharacterList.json")
Character.SaveCharacter(Skull,"CharacterList.json")


rarity5 =[]
rarity4=[]
rarity3=[]
def sort_rarity():
    with open ("CharacterList.json", 'r+') as Retrive_CharacterList:
        Existing_Character = json.load(Retrive_CharacterList)
        if all("name" in character for character in Existing_Character):
            for character in Existing_Character:
                if character['rarity'] == 5:
                    rarity5.append({"name": character['name'], "rarity": character['rarity']})
                elif character['rarity'] == 4:
                    rarity4.append({"name": character['name'], "rarity": character['rarity']})
                else:
                    rarity3.append({"name": character['name'], "rarity": character['rarity']})
        else:
            print("something is wrong")
    
print(rarity3)
print(rarity4)
print(rarity5)