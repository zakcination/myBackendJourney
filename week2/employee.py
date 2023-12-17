from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    id: int
    salary: float
    department: str

    def __eq__(self, other):
        return self.id == other.id

    def give_raise(self, amount):
        self.salary += amount
        return self.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __str__(self) -> str:
        return (f" |+ Employee +|\n"
                f" |+++ Name: {self.name}\n"
                f" |+++ ID: {self.id}\n"
                f" |+++ Salary: {self.salary}\n"
                f" |+++ Department: {self.department}\n"
                )
