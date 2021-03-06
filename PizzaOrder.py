# PizzaOrder.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        OD = "******\n"
        OD += "Order Time: {}\n".format(self.time)
        
        TotalPrice = 0.0
        for pizza in self.pizzas:
            OD += pizza.getPizzaDetails() + "\n----\n"
            TotalPrice += pizza.getPrice()

        OD += "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(TotalPrice)
        return OD

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






