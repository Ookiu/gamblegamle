from CharacterLibary import Character
from CharacterLibary import Enemy
from CharacterLibary import Actions
import json
#filename is for character "CharacterList.json" and enemy is "enemyList.json"

wolf = Enemy("wolf",2000,50,"beast")
Enemy.Save_Enemy(wolf)
Jax = Character("Jax",1000,100,5)
Character.Save_Character(Jax)
Saber = Character("Saber",2000,20,4)
Character.Save_Character(Jax)
Skull = Character("Skull",800,200,3)
Character.Save_Character(Skull)



