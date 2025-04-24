class Animal:
    def crier(self):
        print("Un cri d'animal")
  
        
class Chien(Animal):
    def crier(self):
        print("Miaouh!")
        
        
class Chat(Animal):
    def crier(self):
        print("Woauf! Woauf!")
        
        
class Inconnu(Animal):
    def crier(self):
        return super().crier()
   
   
animal = Animal()
print(animal.crier())

chat = Chat()
print(chat.crier())

chien = Chien()
print(chien.crier())

inconnu = Inconnu()
print(inconnu.crier())
