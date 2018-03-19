class FruitPack:

    def __init__(self):
        self.fruits = [
            "Strawberry", "Grape", "Kiwifruit", "Blackberry", "Orange", "Watermelon", "Apple", "Lemon", "Papaya", "Cherry"
        ]

    def __len__(self):
        return len(self.fruits)

    def __getitem__(self, position):
        return self.fruits[position]
