import datetime


class Person:

    @staticmethod
    def get_min_age():
        return 16

    @classmethod
    def is_staff(cls):
        print('Called is_Staff', cls)
        return cls != Student

    @classmethod
    def __new__(cls, *args, **kwargs):
        print('called __new__', cls)
        return super().__new__(cls)

    def __init__(self, person_id: str, name: str, birth_date: datetime.date):
        print('called __init__')
        self.person_id = person_id
        self.name = name
        self.birth_date = birth_date

    def get_age(self):
        return datetime.date.today().year - self.birth_date.year


class Lecturer(Person):
    pass
class LeadLecturer(Lecturer):
    pass
class Employee(Person):
    pass
class Student(Person):
    pass



if __name__ == '__main__':
    p = Person('a', 'b', datetime.date(2000,11,11))
    p.get_age()
    Person.get_age(p)
    # print(p)
    l = Lecturer('a', 'b', datetime.date(2000,11,11))
    l.is_staff()
    # Person.get_min_age()
    l.get_min_age()