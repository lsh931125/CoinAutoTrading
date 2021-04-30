class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

cusT1 = Customer(1, "lee")
cusT2 = Customer(2, "park")
print(cusT1.id,cusT1.name)
print(cusT2.id,cusT2.name)