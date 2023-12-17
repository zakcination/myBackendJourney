from dataclasses import dataclass
from Employee import Employee
from Task import Task
from decorators import log_decorator
from decorators import tasks_validation_decorator
from decorators import timing_decorator


@dataclass
class Project:
    _name: str
    _description: str
    _budget: float
    _team_members: list
    _tasks: list
    _duration: str = None

    @staticmethod
    def validate_budget(budget):
        if float(budget) < float(100000):
            raise ValueError("Budget cannot be Less than 100 000 tenge")
        return budget

    @classmethod
    @log_decorator
    @timing_decorator
    def create_project(cls, name, description, budget, duration,
                       team_members=None, tasks=None):
        cls.validate_budget(budget)
        return cls(_name=name, _description=description,
                   _duration=duration, _budget=budget,
                   _team_members=team_members
                   if team_members is not None
                   else [],
                   _tasks=tasks
                   if tasks is not None
                   else [])

    def set_description(self, description: str):
        self._description = description

    def set_duration(self, duration: str):
        self._duration = duration

    def add_team_member(self, team_member: Employee):
        if self._team_members is None:
            self._team_members = []
        self._team_members.append(team_member)

    def set_budget(self, budget: float):
        self._budget = budget

    def add_task(self, task: Task):
        if self._tasks is None:
            self._tasks = []
        self._tasks.append(task)

    def __repr__(self):
        return (f"===== Project: =======\n"
                f" |= Name: {self._name}\n"
                f" |= Description: {self._description}\n"
                f" |= Budget: {self._budget}\n"
                f" |= Duration: {self._duration}\n"
                f""" |= Team Members: \n{chr(10).join(str(member)
                        for member in self._team_members)}\n"""
                f""" |= Tasks: \n{chr(10).join('  ' + str(task)
                        for task in self._tasks)}\n""")

    @log_decorator
    @tasks_validation_decorator
    def task_generator(self):
        for task in self._tasks:
            yield task

    def high_priority_task_generator(self):
        for task in self._tasks:
            if task.priority == 'high':
                yield task

    def task_report_generator(self):
        for task in self._tasks:
            yield str(task)
