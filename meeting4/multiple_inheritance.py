from pydantic import BaseModel


class Person:
    def get_id(self):
        return 123456789


class Student(Person):
    def get_grades(self):
        return [100, 90]

    def get_id(self):
        return 200


class Employee(Person):
    def __init__(self):
        self.salary = 10000

    def get_id(self):
        return 100


class WorkingStudent(Student, Employee):
    pass


class Lecturer(Person, JsonSerialization, XmlSerialization)

if __name__ == '__main__':
    p = WorkingStudent()
    print(p.salary)
    print(p.get_grades())
    print(p.get_id())
    # print(mro(p.get_id.mro))
    print(WorkingStudent.mro())