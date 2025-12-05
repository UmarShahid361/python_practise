# class Product:
#     def __init__(self, name, price, in_stock):
#         self.name = name
#         self.price = price
#         self.in_stock = in_stock

#     def __repr__(self):
#         return f"{self.name} {self.price} {self.in_stock}"


# p = Product("Laptop", 299, True)
# print(p)

from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
    in_stock: bool
    tags: list[str]


p = Product("LAPTOP", 99.9, False)
print(p)
