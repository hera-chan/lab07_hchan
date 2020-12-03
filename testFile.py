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
           '******\nOrder Time: 102027\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ anchovies\n\t+ bacon\nPrice: $11.50\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Best\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $23.50\n******\n'
    
def test_OrderQueue():

    cp2 = CustomPizza("M")
    cp2.addTopping("anchovies")
    cp2.addTopping("bacon")
    sp1 = SpecialtyPizza("S", "Best")
    order1 = PizzaOrder(102027)
    order1.addPizza(cp2)
    order1.addPizza(sp1)

    cp1 = CustomPizza("M")
    order2 = PizzaOrder(171820)
    order2.addPizza(cp1)


    sp2 = SpecialtyPizza("L", "Worst")
    cp3 = CustomPizza("L")
    cp3.addTopping("cheese")
    cp3.addTopping("peewee")
    cp3.addTopping("omg")
    cp3.addTopping("chill")
    sp3 = SpecialtyPizza("M", "Mediocre")
    order3 = PizzaOrder(202222)
    order3.addPizza(sp2)
    order3.addPizza(cp3)
    order3.addPizza(sp3)


    sp4 = SpecialtyPizza("S", "Hera")
    order4 = PizzaOrder(142020)
    order4.addPizza(sp4)


    oq = OrderQueue()
    oq.addOrder(order1)
    oq.addOrder(order2)
    oq.addOrder(order3)
    oq.addOrder(order4)

    assert oq.processNextOrder() == '******\nOrder Time: 102027\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ anchovies\n\t+ bacon\nPrice: $11.50\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Best\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $23.50\n******\n'
    assert oq.processNextOrder() == '******\nOrder Time: 142020\nSPECIALTY PIZZA\nSize: S\nName: Hera\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $12.00\n******\n'
    assert oq.processNextOrder() == '******\nOrder Time: 171820\nCUSTOM PIZZA\nSize: M\nToppings:\nPrice: $10.00\n\n----\nTOTAL ORDER PRICE: $10.00\n******\n'
    assert oq.processNextOrder() == '******\nOrder Time: 202222\nSPECIALTY PIZZA\nSize: L\nName: Worst\nPrice: $16.00\n\n----\nCUSTOM PIZZA\nSize: L\nToppings:\n\t+ cheese\n\t+ peewee\n\t+ omg\n\t+ chill\nPrice: $16.00\n\n----\nSPECIALTY PIZZA\nSize: M\nName: Mediocre\nPrice: $14.00\n\n----\nTOTAL ORDER PRICE: $46.00\n******\n'


    










    
