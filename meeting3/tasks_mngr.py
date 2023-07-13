import time
from concurrent.futures import ThreadPoolExecutor, Future
from subprocess import Popen
from threading import Event

from pydantic import BaseModel


class Task(BaseModel):
    id: str
    in_file: str
    out_file: str
    status: str

class TasksMngr:
    def __init__(self):
        self.tasks: dict[str, Task] = {}
        self.executor = ThreadPoolExecutor()
        self.futures: dict[str, Future] = {}
        self.events: dict[str, Event] = {}


    @staticmethod
    def convert(task, cancelled_event: Event):
        cmd = ['ffmpeg', '-i', task.in_file, task.out_file]
        p = Popen(cmd)

        while True:
            try:
                p.wait(1)
                task.status = 'completed'
                break
            except TimeoutError:
                if cancelled_event.is_set():
                    print('killing task ', task.id)
                    p.kill()
                    task.status = 'cancelled'
                    break
        # while p.returncode is None:
        #     if cancelled_event.is_set():
        #         print('killing task ', task.id)
        #         p.kill()
        #     time.sleep(1)
        # p.wait()

        print(f'task {task} completed')

    def run_conversion(self, in_file: str, task_id):
        task = Task(id=task_id, in_file=in_file, status='in_process', out_file=in_file.replace('.mp4', '.mp3'))
        self.tasks[task.id] = task
        cancelled_event = Event()
        self.events[task_id] = cancelled_event
        future = self.executor.submit(TasksMngr.convert, task, cancelled_event)
        self.futures[task_id] = future
        return task

    def get_task_status(self, task_id):
        return self.tasks[task_id].status

    def cancel_task(self, task_id):
        print('Requested to cancel task', task_id)
        future = self.futures[task_id]
        is_cancelled = future.cancel()
        if is_cancelled:
            self.tasks[task_id].status = 'cancelled'
        else:
            self.events[task_id].set()
