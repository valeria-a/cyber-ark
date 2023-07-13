class CyberArkClass(type):

    def __new__(mcs, *args, **kwargs):
        if len(args[0]) > 10:
            raise Exception('Too long class name')
        return super().__new__(mcs, *args, **kwargs)

class Good(metaclass=CyberArkClass):
    pass


class BadBadBadBad(metaclass=CyberArkClass):
    pass