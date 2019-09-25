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

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_attack = 0
        for abilities in self.abilities:
            attack = abilities.attack()
            total_attack = total_attack + attack
            return total_attack

    def add_armor(self, armor):
        self.armors = armor  

    def defend(self, damage_amt):
        self.damage_amt = damage_amt
        for armor in self.armors:
            block = armor.block()
            total_block = total_block + block
            return total_block





if __name__ == "__main__":
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
    # print(hero.abilities)

    
    