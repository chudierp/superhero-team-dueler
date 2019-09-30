import random
random.randint(2,7)

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return random.randint(0,self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health 
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_attack = 0
        if len(self.abilities) > 0:
            for ability in self.abilities:
                attack = ability.attack()
                total_attack += attack
                return total_attack
        else:
            return 0
        

    def add_armor(self, armor):
        # self.armors = armor 
        self.armors.append(armor) 

    def defend(self):
        # self.damage_amt = damage_amt
        if len(self.armors) == 0:
            return 0

        for armor in self.armors:
            block = armor.block()
            total_block = 0
            total_block = total_block + block
            return total_block


    def take_damage(self, damage):
        self.damage = damage
        block_damage = self.defend()
        damage -= block_damage
        self.current_health -= damage
        # return self 

    def is_alive(self):
        if self.current_health > 0: 
            return True
        return False    

    def fight(self, opponent):   
        while (self.is_alive()== True and opponent.is_alive() == True):
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

            if opponent.current_health < self.attack():
               opponent.is_alive() == False
               print(self.name + " won! ")
            elif self.current_health < opponent.attack():
                self.is_alive() == False
                print(opponent.name + " won! ")   

class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength//2, self.attack_strength)

class Team(Hero): 
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        else:
            return 0    

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)





                     

  

if __name__ == "__main__":
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())
    # print(hero.abilities)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)



    
    