import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))  # create random 12 characters string


@dataclass
class Person:
    name: str
    address: str
    active: bool = True
    # we use this construction to avoid the situation when all objects of class Person will refer to the same list
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == '__main__':
    main()
