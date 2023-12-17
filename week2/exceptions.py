
class InvalidPriorityError(Exception):
    def __init__(self, priority):
        self.priority = priority
        self.message = f"""Invalid priority: {self.priority}.
         Priority must be 'high' or 'low'."""
        super().__init__(self.message)


class InvalidDeadlineError(Exception):
    def __init__(self, deadline):
        self.deadline = deadline
        self.message = f"""Invalid deadline: {self.deadline}.
         Deadline must be in the future."""
        super().__init__(self.message)


class InvalidPaymentError(Exception):
    def __init__(self, payment):
        self.payment = payment
        self.message = f"""Invalid payment: {self.payment}.
         Payment must be a positive value."""
        super().__init__(self.message)
