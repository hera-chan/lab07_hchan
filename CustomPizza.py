# CustomPizza.py

from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if size == "S":
            self.price = 8.00
        elif size == "M":
            self.price = 10.00
        elif size == "L":
            self.price = 12.00
        
    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.price += 0.50
        elif self.size == "M":
            self.price += 0.75
        elif self.size == "L":
            self.price += 1.00

    def getPizzaDetails(self):
        PizzaDetails = "CUSTOM PIZZA\nSize: {}\nToppings:".format(self.size)
        if len(self.toppings) != 0:
            for topping in self.toppings:
                PizzaDetails += "\n\t+ {}".format(topping)
        PizzaDetails += "\nPrice: ${:.2f}\n".format(self.price)
        return PizzaDetails
