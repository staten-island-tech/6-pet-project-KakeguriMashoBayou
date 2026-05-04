class Pokemon:
    def __init__(self, name, strength, speed, energy, hunger):
        self.name = name
        self.__strength = strength
        self.__speed = speed
        self.__energy = energy
        self.__hunger = hunger

    def dead(self):
        return self.__energy <= 0 or self.__hunger <=0

    def __limit_stats(self):
        self.__strength = max(0,min(self.__strength, 100))
        self.__speed = max(0,min(self.__speed,100))
        self.__hunger = max(0,min(self.__hunger,100))
        self.__energy = max(0,min(self.__energy, 100))
                        

    def workout(self):
         self.__strength += 20
         self.__energy -= 5
         self.__hunger -=10
         self.__limit_stats()
         print(f"you played with {self.name}!")
         if self.__energy <= 8:
             print("your pet is way to tired to keep going")
      
    def cardio(self):
        self.__speed += 20
        self.__energy -=10
        self.__hunger -=5
        self.__limit_stats()
        print(f"{self.name} is working on the treadmill !")

    def rest(self):
        self.__energy +=20
        self.__hunger -=10
        self.__limit_stats()
        print(f"{self.name} is currently sleeping")

    def feasting(self):
        self.__hunger +=35
        self.__energy +=10
        self.__limit_stats()

    def show_status(self):
        print("---THIS IS YOUR PETS STATUS---")
        print(f"Name :{self.name}")
        print(f"strength: {self.__strength}")
        print(f"Hunger: {self.__hunger}")
        print(f"Energy: {self.__energy}")
        print(f"Speed: {self.__speed}")
      
import random
print("Hi, this is a pokemon simulator where you raise your pokemon!")
pokemon_name = input("What is your pokemons name?: ")

strength1 = random.randint(10,100)
speed1 = random.randint(10,100)
energy1 = random.randint(10,100)
hunger1 = random.randint(10,100)
my_pokemon = Pokemon(pokemon_name, strength1, speed1, hunger1, energy1)
while True:
    my_pokemon.show_status()

    print("what would you like to do with your pokemon?")
    print("1. workout")
    print("2. Cardio")
    print("3. rest")
    print("4. feasting")
    print("5. Leave the Game")
    choice = input("Choose between the five numbers!: ")

    if choice == "1":
        my_pokemon.workout()
        if my_pokemon.dead():
            print(f"{pokemon_name} is dead, its hunger or energy has reached 0")
            break
    elif choice == "2":
        my_pokemon.cardio()
        if my_pokemon.dead():
            print(f"{pokemon_name} is dead, its hunger or energy has reached 0")
            break
    elif choice == "3":
       my_pokemon.rest()
       if my_pokemon.dead():
            print(f"{pokemon_name} is dead, its hunger or energy has reached 0")
            break
    elif choice == "4":
         my_pokemon.feasting()
         if my_pokemon.dead():
            print(f"{pokemon_name} is dead, its hunger or energy has reached 0")
            break
    elif choice == "5":
        print(f"Bye hope u enjoyed.")
        break
    else:
        print("I dont think thats possible, insert another one")