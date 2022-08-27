class Food:
    types = "all"
    #methods like __init__ and __str__ are called dunder methods because they begin and end with double underscores.
    def __init__(self,name,classes,benefit):
        self.name = name
        self.classes = classes
        self.benefit = benefit
    def get_name (self):
        return  #f"{self.name} is a {self.classes} and gives {self.benefit}"   self.name,self.classes,self.benefit    
food_1 = Food ("egg","bodybuilder","strongbones")
food_2 = Food ("apple","vegetable","strongimmune") 
# print(food_1.get_name())
# print(food_2.get_name())
for food in (food_1, food_2):
    print(f"{food.name} is a {food.classes} and gives {food.benefit}")       
