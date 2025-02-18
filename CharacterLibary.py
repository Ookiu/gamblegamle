import json

class entity:
    def __init__(self,name,hp,atk,):
        self.name= name
        self.hp = hp
        self.atk = atk

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk
    
    def assign_atk(self,atk):
        self.atk = atk

    def assign_hp(self,hp):
        self.hp = hp

    def make_character():
        pass

    def make_enemy():
        pass

class Character(entity):
    def assign_rarity(self,rarity):
        self.rarity = rarity

    def get_rarity(self):
        return self.rarity
    
    def SaveCharacter(character,filename): 
        try:
            with open(filename, 'r') as characterList:
                file = json.load(characterList)
        except (FileNotFoundError, json.JSONDecodeError):
            file = []

        if not any(char["name"] == character.name for char in file):
            new_character = {
                "name": character.name,
                "hp": character.hp,
                "atk": character.atk,
                "rarity": character.get_rarity()}
            file.append(new_character)
            
            with open(filename, 'w') as characterList:
                json.dump(file, characterList, indent=4)
                
    def sort_rarity(filename="CharacterList.json"):
        rarity5 = []
        rarity4 = []
        rarity3 = []

        try:
            with open(filename, 'r') as file:
                existing_characters = json.load(file)
        except FileNotFoundError:
            return "Error: File not found."
        except json.JSONDecodeError:
            return "Error: Invalid JSON format."

        if not all(isinstance(character, dict) and "name" in character and "rarity" in character for character in existing_characters):
            return "Error: Invalid character data format."

        for character in existing_characters:
            rarity = character['rarity']
            name = character['name']
            if rarity == 5:
                rarity5.append({"name": name, "rarity": rarity})
            elif rarity == 4:
                rarity4.append({"name": name, "rarity": rarity})
            else:
                rarity3.append({"name": name, "rarity": rarity})

        sorted(rarity3, key=lambda x: x["name"]), sorted(rarity4, key=lambda x: x["name"]), sorted(rarity5, key=lambda x: x["name"])
        print(rarity3)
        print(rarity4)
        print(rarity5)
        return rarity3, rarity4, rarity5

    def retrive_all_character():
        pass
        
class Enemy(entity):
    def enemy_type(self,etype):
        self.etype = etype

    def get_type(self):
        return self.etype

    def enemy(enemy, filename): 
        try:
            with open(filename, 'r') as enemyList:
                file = json.load(enemyList)
        except (FileNotFoundError, json.JSONDecodeError):
            file = []

        if not any(enemy["name"] == enemy.name for enemy in file):
            new_enemy = {
                "name": enemy.name,
                "hp": enemy.hp,
                "atk": enemy.atk,
                "type": enemy.get_type()}
            file.append(new_enemy)
            
            with open(filename, 'w') as characterList:
                json.dump(file, characterList, indent=4)
       
class Actions:
    @staticmethod
    def attack(character, enemy):
        remaining_hp = enemy.get_hp() - character.get_atk()
        enemy.hp = max(0, remaining_hp)
        print(f"{enemy.name} has {enemy.hp} hp left.")

