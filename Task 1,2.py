# class Technic:
#     __slots__ = ('name', 'price', 'availability', 'category')
#
#     def __init__(self, name: str, price: int, availability: bool):
#         self.name = name
#         self.price = price
#         self.availability = availability
#         self.category = "Budget" if self.price < 1000 else "Expensive"

from functools import total_ordering
from dataclasses import dataclass


@dataclass(frozen=True)
@total_ordering
class Technic:
    name: str
    price: float
    availability: bool

    @property
    def category(self) -> str:
        return "Budget" if self.price < 5000 else "Expensive"

    def __eq__(self, other):
        return len(self.name) == len(other.name)

    def __lt__(self, other):
        return len(self.name) < len(other.name)
