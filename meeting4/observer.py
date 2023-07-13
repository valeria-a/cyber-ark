from abc import ABC, abstractmethod


# subject
class Observable:
    def __init__(self):
        # subscribers
        self._observers = []

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, **kwargs):
        for observer in self._observers:
            observer.update(**kwargs)


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError()
