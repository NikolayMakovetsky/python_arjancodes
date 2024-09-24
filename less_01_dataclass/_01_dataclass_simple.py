# Data class = data oriented class
# It's for representing a point, a vector or any kind of data structure

import random
import string


def gererate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))  # create random 12 characters string


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{__class__.__name__}: name={self.name}, address={self.address}"


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == '__main__':
    main()
