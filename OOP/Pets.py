#1. Create a Class for Pets:
#Task: Create a Python class called `Pet` with attributes such as `name`, `age`, and `species`.
# Then, write methods to set and get each attribute, as well as a method to display all information about the pet.

class Pets:
    def __init__(self, name, specie, color, age, owner):
        self.name = name
        self.specie = specie
        self.color = color
        self.age = age
        self.owner = owner
    def __str__(self):
        return f"The name is {self.name}. A {self.color} {self.specie} and {self.age} years old. {self.owner} is The Owner's name."
    
    # def start(self):
    #     print(f"The name is {self.name}. A {self.color} {self.specie} and {self.age} years old. {self.owner} is The Owner's name.")
    

my_pet = Pets("Ivy", "cat", "white", 1, "Zoey")
friend_0pet = Pets("Theo", "cat", "marmalade", 2, "Luka")
friend_1pet = Pets("Duke", "dog", "Black", 2, "Elizabeth")
friend_2pet = Pets("Grace", "hamster", "brown", 3, "Luis")

print(my_pet, friend_0pet, friend_1pet, friend_2pet, sep='\n')
