class Cat:
    def __init__(self, name, age, color, food):

        self.name = name
        self.age = age
        self.color = color
        self.food = food

    def house(self, house):
        self.house = house
lol = Cat("Drishya", 18 , "Red", "Fish")

print(lol.name)

print(lol.age)

lol.house("Hut")

print(lol.house)
