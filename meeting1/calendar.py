import datetime


class Calendar:
    def __init__(self, start: datetime.date, end: datetime.date):
        self._start = start
        self.end = end
        self._tasks: dict[datetime.date, list[str]] = {}
        self._curr: datetime.date = None

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, new_start):
        if new_start >= self.end:
            raise ValueError()
        else:
            self._start = new_start

    def get_tasks_num(self):
        return sum(map(lambda e: len(e), self._tasks.values()))

    def add_task(self, task_date, task):
        self._tasks.setdefault(task_date, []).append(task)

    def __iter__(self):
        self._curr = sorted(list(self._tasks.keys()))[0]
        return self

    def __next__(self):
        if not self._curr:
            raise StopIteration()
        ret_val = self._curr, self._tasks[self._curr]
        sorted_dates = sorted(list(self._tasks.keys()))
        last_index = sorted_dates.index(self._curr)
        if last_index < len(sorted_dates)-1:
            self._curr = sorted_dates[last_index+1]
        elif last_index == len(sorted_dates)-1:
            self._curr = None
        else:
            raise StopIteration()
        return ret_val

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    c = Calendar(datetime.date.today(),
                 datetime.date.today() + datetime.timedelta(weeks=1))
    print(c.start)
    c.start = datetime.date.today()
    print(c.get_tasks_num())
    c.add_task(datetime.date(2023, 7, 5), "buy apples")
    c.add_task(datetime.date(2023, 7, 5), "lecture")
    c.add_task(datetime.date(2023, 7, 7), "sport")
    c.add_task(datetime.date(2023, 7, 8), "order vacation")
    for i in c:
        print(i)
    # l = [1,2,3,4]
    # iterator = l.__iter__()
    # print(iterator.__next__())
    # print(iterator.__next__())
    # print(iterator.__next__())
    # print(iterator.__next__())
    # print(iterator.__next__())