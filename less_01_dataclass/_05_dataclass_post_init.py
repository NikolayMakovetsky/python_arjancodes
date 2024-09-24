import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    # If we want to generate a value from the other instance variables
    # We can use __post_init__ to create extra fields
    search_string: str = field(init=False)

    def __post_init__(self) -> None:
        self.search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == '__main__':
    main()
