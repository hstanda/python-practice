class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def details(self):
        print("Fruit " + self.name + " has " + self.color + " colour")

apple = Fruit("Apple", "Red")
apple.details()
