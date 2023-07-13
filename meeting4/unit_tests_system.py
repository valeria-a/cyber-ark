import random

from meeting4.observer import Observable, Observer


class UnitTest(Observable):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run_test(self):
        # call the actual api
        num = random.randint(1,5)
        if num % 2 == 0:
            print(f'Test {self.name} failed, notifying subscribers')
            self.notify(test_name=self.name)
            return False
        print(f"Test passed {self.name}")
        return True

class Developer(Observer):

    def __init__(self, email):
        self.email = email

    def update(self, *args, **kwargs):
        print(f'sending email to {self.email} about failed test {kwargs}')

class Report(Observer):

    def __init__(self):
        self.failed_tests = []

    def update(self, *args, **kwargs):
        self.failed_tests.append(kwargs['test_name'])

    def create_final_report(self):
        print(f'Final report:\n{self.failed_tests}')

if __name__ == '__main__':
    unit_tests = [UnitTest(name) for name in ('test1', 'test2', 'test3')]
    john = Developer('john@gmail.com')
    unit_tests[0].subscribe(john)

    report = Report()
    david = Developer('david@gmail.com')
    for t in unit_tests:
        t.subscribe(david)
        t.subscribe(report)

    for t in unit_tests:
        t.run_test()

    report.create_final_report()





