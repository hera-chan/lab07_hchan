# testFile.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_Pizza():
    p1 = Pizza("S")
    assert p1.getPrice() == 0.0
    p1.setPrice(2.00)
    assert p1.getPrice() == 2.00
    p1.setSize("M")
    assert p1.getSize() == "M"

def test_CustomPizza():
    # no toppings
    cp1 = CustomPizza("M")
    assert cp1.getPizzaDetails() == \
           'CUSTOM PIZZA\nSize: M\nToppings:\nPrice: $10.00\n'

    # toppings
    cp2 = CustomPizza("M")
    cp2.addTopping("anchovies")
    cp2.addTopping("bacon")
    assert cp2.getPizzaDetails() == \
           'CUSTOM PIZZA\nSize: M\nToppings:\n\t+ anchovies\n\t+ bacon\nPrice: $11.50\n'
    
def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Best")
    assert sp1.getPizzaDetails() == \
           'SPECIALTY PIZZA\nSize: S\nName: Best\nPrice: $12.00\n'

    sp2 = SpecialtyPizza("L", "Worst")
    assert sp2.getPizzaDetails() == \
           'SPECIALTY PIZZA\nSize: L\nName: Worst\nPrice: $16.00\n'

def test_PizzaOrder():
    cp2 = CustomPizza("M")
    cp2.addTopping("anchovies")
    cp2.addTopping("bacon")
    sp1 = SpecialtyPizza("S", "Best")
    order = PizzaOrder(171823)
    order.addPizza(cp2)
    order.addPizza(sp1)
    assert order.getTime() == 171823
    order.setTime(102027)
    assert order.getTime() == 102027
    assert order.getOrderDescription() == \
           '******\nOrderTime: 102027\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ anchovies\n\t+ bacon\nPrice: $11.50\n----\nSPECIALTY PIZZA\nSize: S\nName: Best\nPrice: $12.00\n----\nTOTAL ORDER PRICE: $23.50\n******\n'
    
def test_OrderQueue():
    oq = OrderQueue()
    oq.addOrder(102027)
    oq.addOrder(101123)
    oq.addOrder(111111)
    oq.addOrder(222222)
    assert oq.processNextOrder() == 101123
    assert oq.processNextOrder() == 102027
    assert oq.processNextOrder() == 111111
    assert oq.processNextOrder() == 222222
    assert oq.processNextOrder() == 101123
    










    
