#object-oriented programming
#is a method of structuring a program by building related properties and behaviours into individual objects.
#creating a new objet from a class is called instantiating
class Animal:
    kingdom = "Sarah"# class attribute
    def __init__(self,name,ability):#instance attribute.
        self.name = name 
        self.ability = ability

    # def get_name_and_ability(self):
    #     return self.name,self.ability

    # def get_name(self):
    #     return self.name
#an instance is an object that is built from a class and contains real data.
animal_1 = Animal("Tiger", "Swimming")
# print(animal_1.get_name_and_ability())
animal_2 = Animal("Lion", "Chewing")
# print(animal_2.get_name_and_ability())
# print(animal_1.get_name())

# animal_1.name = "my princess"
# print(animal_1.get_name())
animal_1.kingdom