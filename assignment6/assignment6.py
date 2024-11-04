# Create a pokemon class, complete with initialization function. Use the data in your file to create pokemon objects for each sample in your data.

class Pokemon:
    #initialize the class with the following attributes
    def __init__(self, dexnum, name, generation, type1, type2, species, height,
                 weight, ability1, ability2, hidden_ability, hp, attack, defense, sp_atk,
                 sp_def, speed, total, ev_yield, catch_rate, base_friendship, base_exp, growth_rate,
                 egg_group1, egg_group2, percent_male, percent_female, egg_cycles, special_group):
        self.dexnum = dexnum
        self.name = name
        self.generation = generation
        self.type1 = type1
        self.type2 = type2
        self.species = species
        self.height = height
        self.weight = weight
        self.ability1 = ability1
        self.ability2 = ability2
        self.hidden_ability = hidden_ability
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.total = total
        self.ev_yield = ev_yield
        self.catch_rate = catch_rate
        self.base_friendship = base_friendship
        self.base_exp = base_exp
        self.growth_rate = growth_rate
        self.egg_group1 = egg_group1
        self.egg_group2 = egg_group2
        self.percent_male = percent_male
        self.percent_female = percent_female
        self.egg_cycles = egg_cycles
        self.special_group = special_group
       

    @classmethod
    def create_list_pokemon(self, data): #class method to create a list of pokemon objects
        #keys for the pokemon attributes that will be used to create the pokemon objects
        keys = ["dexnum", "name", "generation", "type1", "type2", "species", "height",
                "weight", "ability1", "ability2", "hidden_ability", "hp", "attack", "defense", "sp_atk",
                "sp_def", "speed", "total", "ev_yield", "catch_rate", "base_friendship", "base_exp", "growth_rate",
                "egg_group1", "egg_group2", "percent_male", "percent_female", "egg_cycles", "special_group"]
       #return a list of pokemon objects the **dict(zip(keys, i)) is used to create the pokemon objects
        return [self(**dict(zip(keys, i))) for i in data]
    

    @classmethod #class method to list the pokemon objects
    def list_pokemon(self, data):
        return self.create_list_pokemon(data)
        
    

def open_pokemon_data(): #function to open the pokemon data file
    try:
        with open("pokemon_data.csv", "r") as file:

            contents = file.read() #reading the contents of the file
            lines = contents.splitlines() #splitting the contents by lines
     #splitting the lines by commas and saving them to a list of columns for my sanity
        columns = [line.split(",") for line in lines] 

        data = columns[1:] #excludes the header

        return data #returns the data
    except FileNotFoundError: #if the file is not found it will print an error message
        print("Error: The file 'pokemon_data.csv' was not found.")

 #`open_pokemon_data` function to open the file and return the data
pokemon_data = open_pokemon_data()
#print(pokemon_data[:3])
#`list_pokemon` function to create a list of pokemon objects
pokemon_objects = Pokemon.list_pokemon(pokemon_data)



#loop to print the pokemon objects
for pokemon in pokemon_objects:
   print(f"""
Dex Number: {pokemon.dexnum}, Name: {pokemon.name}, Generation: {pokemon.generation}
Type 1: {pokemon.type1}, Type 2: {pokemon.type2}, Species: {pokemon.species}
Height: {pokemon.height}, Weight: {pokemon.weight}
Ability 1: {pokemon.ability1}, Ability 2: {pokemon.ability2}, Hidden Ability: {pokemon.hidden_ability}
HP: {pokemon.hp}, Attack: {pokemon.attack}, Defense: {pokemon.defense}, Special Attack: {pokemon.sp_atk}, Special Defense: {pokemon.sp_def}, Speed: {pokemon.speed}
Total: {pokemon.total}, EV Yield: {pokemon.ev_yield}, Catch Rate: {pokemon.catch_rate}, Base Friendship: {pokemon.base_friendship}, Base Experience: {pokemon.base_exp}, Growth Rate: {pokemon.growth_rate}
Egg Group 1: {pokemon.egg_group1}, Egg Group 2: {pokemon.egg_group2}
Percent Male: {pokemon.percent_male}, Percent Female: {pokemon.percent_female}, Egg Cycles: {pokemon.egg_cycles}, Special Group: {pokemon.special_group}
""")