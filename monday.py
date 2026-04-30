import random
name = input("What is your pokemon name?: ")
status_list = ["paralysed", "poisoned", "burned", "frozen" ]

class Pokemon: 
   def __init__(self, name, health, hunger, status, energy):
      self.name = name
      self.__health = health  
      self.__hunger = hunger        
      self.__status = status
      self.__energy = energy
        
 
   def the_status(self):
      if self.__status in status_list:
         self.__health -= 20
         print("health:", self.__health)
     
      self.__health = max(0, min(100, self.__health))
      if self.__health <=0:
         print("your pokemon is dead, dig a grave for it")
      elif self.__health <30:
         print("your pokemon is severly damaged")
      elif self.__health <80:
         print("your pokemon has a bruise")

random_status = random.choice(status_list)




            

