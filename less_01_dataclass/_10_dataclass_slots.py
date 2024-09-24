# Слоты в Python dataclasses позволяют задать для классов чётко фиксированное число свойств.
# Это может увеличить скорость обработки классов и уменьшить объём используемой ими памяти.

import timeit
from dataclasses import dataclass
from functools import partial


@dataclass(slots=False)
class Person:
    name: str
    address: str
    email: str


@dataclass(slots=True)
class PersonSlots:
    name: str
    address: str
    email: str


# class PersonEmployee(PersonSlots, EmployeeSlots):
#     pass


def get_set_delete(person: Person | PersonSlots):
    person.address = "123 Main St"
    person.address
    del person.address



def main():
    person = Person("John", "123 Main St", "kkk@mail.ru")
    person_slots = PersonSlots("John", "123 Main St", "kkk@mail.ru")
    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1_000_000))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=1_000_000))
    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")


if __name__ == '__main__':
    main()
