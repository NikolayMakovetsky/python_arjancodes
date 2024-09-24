# Structural pattern matching в Python — это механизм, который проверяет,
# соответствует ли значение выражения заданной структуре (образцу)

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


# match_args=True means that dataclass is support "structural pattern matching"
@dataclass(match_args=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == '__main__':
    main()
