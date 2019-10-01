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
        self.deaths = 0
        self.kills = 0

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

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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

        if opponent.current_health <= 0:
            opponent.is_alive() == False
            self.add_kill(1)
            opponent.add_deaths(1)
            print(self.name + " won! ")
        else:
            self.add_deaths(1)
            opponent.add_kill(1)
            print(opponent.name + " won! ")  

    def add_kill(self, num_kills):
         self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

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

    def attack(self, other_team):
        hero = random.choice(self.heroes)
        opponent = random.choice(other_team.heroes)
        hero.fight(opponent)

    def revive_heroes(self, health=100):
        # Hero.health = health
        for hero in self.heroes:
            hero.health = health

    def stats(self):
        print("Here are the team stats: \n")
        for hero in self.heroes:
            print("Name: " + hero.name, "Kills: " + str(hero.kills),"Deaths: " + str(hero.deaths))
            for ability in hero.abilities:
                print(ability.name)
            for armor in hero.armors:
                print(armor.name)    

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Enter a new ability: ")
        attack_strength = input("Enter ability strength: ")
        ability = Ability(name, int(attack_strength))
        return ability

    def create_weapon(self):
        name = input("Enter a new weapon: ")
        attack_strength = input("Enter attack strength: ")
        weapon = Weapon(name, int(attack_strength))
        return weapon

    def create_armor(self):
        name = input("Enter a new armor: ")
        max_block = input("Enter maximum block strength: ") 
        armor = Armor(name, int(max_block))  
        return armor 

    def create_hero(self): #have someone look over this
        Hero.name = input("Let's create a hero. Enter a name to call your hero: ")
        hero = Hero(Hero.name, starting_health = 100)
        print(f"Would you like to add armor, abilities, or weapons to your hero {hero.name}?: ")
        user_input = input("Enter 'A' for armor, 'W' for weapons, or 'B' for abilities: ")
        user_input = user_input.upper()
        if user_input == 'A':
            armor = self.create_armor()
            hero.add_armor(armor)
        elif user_input == 'W':
            weapon = self.create_weapon()
            hero.add_weapon(weapon)
        elif user_input == 'B':
            ability = self.create_ability()
            hero.add_ability(ability)
        else:
            print ("Invalid response")
        return hero 

    def build_team_one(self):
        name = input("Create a name for team one: ")
        self.team_one = Team(name)
        team_one_size = int(input("How many heroes do you want on your first team?: "))
        for hero in range(team_one_size):
            self.team_one.heroes.append(self.create_hero())

    def build_team_two(self):
        name = input("Create a name for team two: ")
        self.team_two = Team(name)
        team_two_size = int(input("How many heroes do you want on your second team?: "))        
        for hero in range(team_two_size):
           self.team_two.heroes.append(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print('\n')
        print("-------------\n")

        self.team_one.stats()
        self.team_two.stats()


        # winning_team = self.team_one.attack(self.team_two)
        # print("The winning team is team {}! Congratulations!".format(winning_team))

        


if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats() 
# # ability = Ability("Debugging Ability", 20)
#     # print(ability.name)
#     # print(ability.attack())
#     # my_hero = Hero("Grace Hopper", 200)
#     # print(my_hero.name)
#     # print(my_hero.current_health)
#     # ability = Ability("Great Debugging", 50)
#     # another_ability = Ability("Smarty Pants", 90)
#     # hero = Hero("Grace Hopper", 200)
#     # hero.take_damage(150)
#     # print(hero.is_alive())
#     # hero.take_damage(15000)
#     # print(hero.is_alive())
#     # shield = Armor("Shield", 50)
#     # hero.add_armor(shield)
#     # hero.take_damage(50)
#     # print(hero.current_health)
#     # hero.add_ability(ability)
#     # hero.add_ability(another_ability)
#     # print(hero.attack())
#     # print(hero.abilities)
#     # hero1 = Hero("Wonder Woman")
#     # hero2 = Hero("Dumbledore")
#     # ability1 = Ability("Super Speed", 300)
#     # ability2 = Ability("Super Eyes", 130)
#     # ability3 = Ability("Wizard Wand", 80)
#     # ability4 = Ability("Wizard Beard", 20)
#     # hero1.add_ability(ability1)
#     # hero1.add_ability(ability2)
#     # hero2.add_ability(ability3)
#     # hero2.add_ability(ability4)
#     # hero1.fight(hero2) 