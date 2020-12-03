# Pizza.py

class Pizza:
    def __init__(self, size):
        self.price = 0.0
        self.size = size

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def __gt__(self, other):
        if self.time > other.time:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.time < other.time:
            return True
        else:
            return False
