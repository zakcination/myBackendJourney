import time


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    return wrapper


def tasks_validation_decorator(func):
    def wrapper(self, *args, **kwargs):
        if not self._tasks:
            raise ValueError("No tasks to generate")
        return func(self, *args, **kwargs)
    return wrapper
