class Vehicle:
    # def __new__(cls, *args, **kwargs):
    #     pass

    def __init__(self, manufacturer, km=0):
        self.manufacturer = manufacturer
        self.km = km
# create fields dynamically from kwargs

if __name__ == '__main__':
    v = Vehicle('mazda')
    print('inside Classes file')
    print(type(v))
