#classes and objects ,understanding classes


class ITEM:
    all = []
    pay_rate = 0.8

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        ITEM.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def discount_for_items(self):
        self.price = self.price * self.pay_rate
        return self.price

    def __repr__(self):
        return f"ITEM('{self.name}', {self.price})"

item1 = ITEM("oneplus", 28000, 3)
item2 = ITEM("sony_vaio", 60000, 2)
item2.pay_rate = 0.5
item3 = ITEM("nothing", 5000, 1)
item4 = ITEM("btspeaker", 400, 4)
item4.pay_rate = 0.4

# Uncomment the lines below to print item details and apply discounts
# print(item1.name, item2.name)
# print(item2.discount_for_items(), item2.price)
# for inst in ITEM.all:
#     print(inst.name)

print(ITEM.all)
