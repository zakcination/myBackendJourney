class my_column(object):
    def __init__(self,column_type) -> None:
        self.column_type = column_type
        self.value = None

    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        if not isinstance(value, self.column_type):
            raise TypeError(f'Expected an {self.column_type}[{value}], got {type(value)}')
        self.value = value

    def __delete__(self, instance):
        del self.value



class Model:
    pass


class User(Model):
    name = my_column(str)
    age = my_column(int)

    def __init__(self, name, age) -> None:
        self.name = str(name)
        self.age = int(age)

    def __str__(self) -> str:
        return f'User(name={self.name}, age={self.age})'

if __name__ == '__main__':
    user = User('John', 20)
    print(user)
    user.name = 'Jack'
    user.age = 21
    print(user)
