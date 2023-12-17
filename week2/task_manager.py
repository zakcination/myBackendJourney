from datetime import datetime
from Employee import Employee
from Project import Project
from Task import Task

employees = [
    Employee("John", 1, 100000, "IT"),
    Employee("Jane", 2, 200000, "IT"),
    Employee("Bob", 3, 300000, "IT"),
    Employee("Alice", 4, 400000, "IT"),
    Employee("Richard", 5, 500000, "IT"),
    Employee("Kate", 6, 600000, "IT"),
    Employee("Robert", 7, 700000, "IT"),
    Employee("Mary", 8, 800000, "IT"),
    Employee("John", 9, 900000, "IT"),
    Employee("Jane", 10, 1000000, "IT"),
]


tasks = [
    Task("Task 1", "Description 1", datetime(2023, 12, 19), "high", 100000),
    Task("Task 2", "Description 2", datetime(2023, 12, 18), "low", 200000),
    Task("Task 3", "Description 3", datetime(2023, 12, 20), "high", 300000),
    Task("Task 4", "Description 4", datetime(2023, 12, 18), "low", 400000),
    Task("Task 5", "Description 5", datetime(2023, 12, 17), "high", 500000),
    Task("Task 6", "Description 6", datetime(2023, 12, 22), "low", 600000),
    Task("Task 7", "Description 7", datetime(2023, 12, 23), "high", 700000),
    Task("Task 8", "Description 8", datetime(2023, 12, 21), "low", 800000),
    Task("Task 9", "Description 9", datetime(2023, 12, 19), "high", 900000),
    Task("Task 10", "Description 10", datetime(2023, 12, 17), "low", 1000000),
]


P1 = Project.create_project("Project 1", "Description 1", 1000000, "1 year")
P2 = Project.create_project("Project 2", "Description 2", 130000, "2 years")


P1.add_team_member(employees[0])
P1.add_team_member(employees[1])
P1.add_team_member(employees[2])
P1.add_team_member(employees[3])


P1.add_task(tasks[0])
P1.add_task(tasks[1])
P1.add_task(tasks[2])


# ==== Testing
print(P1)
# P2.task_generator()


# ==== Works fine
# print(employees[3])
# employees[3].give_raise(100000)
# print(employees[3])


# ==== Works fine
# print(employees[3].salary,  employees[2].salary)
# print(employees[3] > employees[2])


# ==== Works fine
# P1.set_description("New Description")
# P1.set_duration("2 years")
# P1.set_budget(2000000)
# P1.add_team_member(employees[4])
# P1.add_task(tasks[3])
# P1.add_task(tasks[4])
# print(P1)


# ==== Works fine
# print(tasks[0])
# tasks[0].set_description("New Description")
# tasks[0].set_deadline(datetime(2023, 12, 18))
# tasks[0].set_priority("low")
# tasks[0].set_payment(1000000)
# print(tasks[0])


# ==== Works fine
# print(Task("Task 10", "Description 10", datetime(2023, 12, 17),\
#  "low", -1000000))


# ==== Works fine
# for task in P1.task_generator():
#     print(task)

# ==== Works fine
