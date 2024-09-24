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
    email_addresses: list[str] = field(default_factory=list)
    # init=False makes impossible to use own id in the __init__ inside @dataclass decorator
    id: str = field(init=False, default_factory=generate_id)  #


def main() -> None:
    person = Person(name="John", address="123 Main St")  # id="53464354" call TypeError
    print(person)


if __name__ == '__main__':
    main()
