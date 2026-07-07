# inheritance

# class animal:
#     def sound(self):
#         print("sound")
# class dog(animal):
#     def bark(self):
#         print("barking..")

# d = dog()
# d.sound()
# d.bark()

# ----------**********----------

# class car:
#     def engine(self):
#         print("engine starts")
# class electriccar(car):
#     def drive(self):
#         print("driving..")

# c = electriccar()

# c.engine()
# c.drive()

# ---------- polymorphism ----------

# class dog:
#     def sound(self):
#         print("barking")
# class cat:
#     def sound(self):
#         print("meowwwww")
# d=dog()
# d.sound()          
# c=cat()
# c.sound()           

# ----------encapsulation----------

# class bank:
#     def __init__(self, name, password):
#         self.name= name
#         self.password=password
#     def display(self):
#         print("name: ",self.name)
#         print("password: ",self.password)
# b=bank("raj", 1234567890)
# b.display()
        
# ----------abstraction ----------

# from abc import ABC, abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class dog:
#     def sound(self):
#         print("barking")
# class cat:
#     def sound(self):
#         print("meowwwww")
# d=dog()
# d.sound()          
# c=cat()
# c.sound()           


