name = input("What is your pokemon name?: ")
status = ["paralysed", "poisoned", "burned", "frozen" ]

class Pokemon: 
   def __init__(self, name, health, hunger, status, energy):
      self.name = name
      self.__health = health  
      self.__hunger = hunger        
      self.__status = status
      self.__energy = energy
        
 
   def status(self):
      if self.__status == status:
         self.__health -= 20
         print(self.__health)
         if self.__health < 60:
            print(self.__health, "your pet is hurt")
         elif self.__health < 30:
            print("your pet needs immediete help")
         else:
            self.__health = 0
            print(self.__health, "your pet is going to see your grandma")
            

