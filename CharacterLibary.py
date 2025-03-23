import json

class entity:
    def __init__(self,name,hp,atk):
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

class Character(entity):
    def __init__(self,name,hp,atk,rarity):
        super().__init__(name,hp,atk)
        self.rarity = rarity

    def assign_rarity(self,rarity):
        self.rarity = rarity

    def get_rarity(self):
        return self.rarity
    
    @staticmethod #because they dont use self
    def Save_Character(character, filename="CharacterList.json"): 
        try:
            with open(filename, 'r') as characterList:
                file = json.load(characterList)
        except (FileNotFoundError, json.JSONDecodeError):
            file = []
        if any(char["name"] == character.name for char in file):
            print(f"Character name '{character.name}' is already taken.")
            return
        new_character = {
            "name": character.name,
            "hp": character.hp,
            "atk": character.atk,
            "rarity": character.get_rarity()}
        file.append(new_character)
        with open(filename, 'w') as characterList:
            json.dump(file, characterList, indent=4)
        print(f"Character '{character.name}' has been saved.")
            
    def Update_existing_character(character,filename="CharacterList.json"): 
        try:
            with open(filename, 'r') as characterList:
                file = json.load(characterList)
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or corrupted.")
            return
        
        Character_found = False
        for char in file:
            if char["name"]== character.name:
                char["name"] = character.name
                char["hp"] = character.hp
                character["atk"] = character.atk
                character["rarity"] = character.get_rarity()
            Character_found = True
            break
        if not Character_found:
            print(f"Character'{character.name}' not found.")    
        else:
            with open(filename, 'w') as characterList:
                json.dump(file, characterList, indent=4)
            print(f"'{character.name}' has been updated.")
                  
    def retrive_all_character():
        pass
        
class Enemy(entity):
    def __init__(self, name, hp, atk,etype):
        super().__init__(name, hp, atk,)
        self.etype = etype

    def assign_enemy_type(self,etype):
        self.etype = etype

    def get_type(self):
        return self.etype

    @staticmethod
    def Save_Enemy(enemy, filename="EnemyList.json"): 
        try:
            with open(filename, 'r') as enemyList:
                file = json.load(enemyList)
        except (FileNotFoundError, json.JSONDecodeError):
            file = []
        if any(e["name"] == enemy.name for e in file):
            print(f"Enemy name '{enemy.name}' is already taken.")
            return
        new_enemy = {
            "name": enemy.name,
            "hp": enemy.hp,
            "atk": enemy.atk,
            "type": enemy.get_type()}
        file.append(new_enemy)
        
        with open(filename, 'w') as enemyList:
            json.dump(file, enemyList, indent=4)
            print("Enemy name taken.")

    @staticmethod
    def Update_existing_enemy(enemy, filename="EnemyList.json"):
        try:
            with open(filename, 'r') as enemyList:
                file = json.load(enemyList)
        except (FileNotFoundError, json.JSONDecodeError):
            print("file doesnt exist or corrupted")
            return
        
        enemy_found = False
        for char in file:
            if char["name"] == enemy.name:
                char["hp"] = enemy.hp
                char["atk"] = enemy.atk
                char["type"] = enemy.get_type()
                enemy_found = True
                break

        if not enemy_found:
            print("Enemy doesnt exist.")
        else:
            with open(filename, 'w') as enemyList:
                json.dump(file, enemyList, indent=4)
            print(f"Enemy '{enemy.name}' has been updated.")    
       
class Actions:
    @staticmethod
    def attack(character, enemy):
        remaining_hp = enemy.get_hp() - character.get_atk()
        enemy.hp = max(0, remaining_hp)
        print(f"{enemy.name} has {enemy.hp} hp left.")

