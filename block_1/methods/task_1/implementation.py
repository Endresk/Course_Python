class Coffee:
    def __init__(self):
        self.espresso = "Эспрессо"
        self.milk = "Молоко"
        self.foam_milk = "Молочная пена"
        self.sugar = "Сахар"
        self.ice_cream = 'Мороженое'

    def cappuccino(self):
        return f"{self.espresso}, {self.milk}"

    def latte(self):
        return f"{self.espresso}, {self.milk}, {self.foam_milk}"

    def glace(self):
        return f"{self.milk}, {self.sugar}, {self.ice_cream}"


if __name__ == '__main__':
    coffe = Coffee()
    print(f"cappuccino structure: {coffe.cappuccino()}")
    print(f"latte structure: {coffe.latte()}")
    print(f"glace structure: {coffe.glace()}")