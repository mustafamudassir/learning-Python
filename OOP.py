# creating a class
class Item:
    def calulate_total_price(self, a, b):
        return a * b
# creating an instance of a class

item1 = Item()

# Assigning attributes

item1.name = "camera"
item1.price = 3000
item1.quantity = 5


# Calling methods from instances of a class:


print(item1.calulate_total_price(item1.price, item1.quantity))

# another exampple (We could create as much as instances we'd like to)

item2 = Item()
item2.name = "phone"
item2.price = 1000
item2.quantity = 3
print(item2.calulate_total_price(item2.price, item2.quantity))