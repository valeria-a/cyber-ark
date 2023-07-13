class Company:
    # def __new__(cls, *args, **kwargs):
    pass


class MyMeta(type):
    def __new__(mcs, *args, **kwargs):
        print("Creating class", mcs, args, kwargs)
        return super().__new__(mcs, *args, **kwargs)

class MyClass(metaclass=MyMeta):
    pass

if __name__ == '__main__':
    c = Company()
    print(type(c))
    print(type(Company))

    Person = type('Person', (), {'max_age': 120})
    print(Person)
    print(Person.max_age)

    my_new = MyMeta('MyNewClass', (), {})
    print(my_new)


class A:
    def save(self):
        pass

class B(A):
    def pre_save(self):
        pass
    def save(self):
        self.pre_save()
        super().save()


class C(B):
    pass

