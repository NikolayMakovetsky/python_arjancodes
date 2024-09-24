import random
import string
from dataclasses import dataclass


def gererate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))  # create random 12 characters string


@dataclass
class Person:
    # __init__ and __repr__ are implemented in @dataclass
    name: str
    address: str


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == '__main__':
    main()
