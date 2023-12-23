from dataclasses import dataclass
from datetime import datetime
from Exceptions import InvalidDeadlineError
from Exceptions import InvalidPaymentError
from Exceptions import InvalidPriorityError


@dataclass
class Task:
    def __init__(self, name, description, deadline, priority, payment):
        self._name = name
        self._description = description
        self._date_created = datetime.now()
        self._deadline = deadline
        self._priority = priority
        self._payment = payment
        self.validate_payment(payment)
        self._suggestion: str = self.calculate_suggestion()

    def calculate_suggestion(self):
        urgency = (self._deadline - datetime.now()).days
        
        #have skipped few(half) cases

        if self._priority == 'high' and urgency <= 2:
            sugg = 'Do this now'
        elif self._priority == 'low' and urgency > 2:
            sugg = 'Eliminate'
        elif self._priority == 'high' and urgency > 2:
            sugg = 'Do this later'
        else:  # self.priority == 'low' and urgency <= 2
            sugg = 'Delegate'
        return sugg

    @staticmethod
    def validate_payment(payment):
        if payment < 0:
            raise ValueError("Payment cannot be Negative")
        return payment

    def set_description(self, description: str):
        self._description = description

    def set_deadline(self, deadline: datetime):
        if deadline < datetime.now():
            raise InvalidDeadlineError(deadline)
        self._deadline = deadline
        self._suggestion = self.calculate_suggestion()

    def set_priority(self, priority: str):
        if priority not in ['high', 'low']:
            raise InvalidPriorityError(priority)
        self._priority = priority
        self._suggestion = self.calculate_suggestion()

    def set_payment(self, payment: float):
        if payment < 0:
            raise InvalidPaymentError(payment)
        self._payment = payment

    def __str__(self):
        return (
            f"\\n"
            f"  |- Task:\n"
            f"  |--- Name: {self._name}\n"
            f"  |--- Description: {self._description}\n"
            f"  |--- Date Created: {self._date_created}\n"
            f"  |--- Deadline: {self._deadline}\n"
            f"  |--- Priority: {self._priority}\n"
            f"  |--- Payment: {self._payment}\n"
            f"  |--- Suggestion: {self._suggestion}\n"
        )
