name = input("What is your pokemon name?: ")
health = 100
status = ["paralysed", "poisoned", "burned", "frozen" ]

class Pokemon: 
   def __init__(self, name, health, hunger, status, energy):
      self.name = name
      self._health = health  
      self._hunger = hunger        
      self._status = status
      self._energy = energy
        
   def status(self):
      if self.__status == status:
         self.__health -= 10
         print(health)

