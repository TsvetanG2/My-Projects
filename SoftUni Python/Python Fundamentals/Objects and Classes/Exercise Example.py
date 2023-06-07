class Bottle:
    def __init__(self, ml, name, color, material="plastic"):
        self.ml = ml
        self.name = name
        self.color = color
        self.material = material

    def open(self):
        print('Opening Bottle')

    def close(self):
        print('Closing Bottle')


bottle1 = Bottle(500, "Devin", "blue", "glass")
bottle2 = Bottle(1500)
print(bottle1.ml)
print(bottle1.open())
print(bottle1.close())