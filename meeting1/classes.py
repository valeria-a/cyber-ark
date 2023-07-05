class Vehicle:
    # def __new__(cls, *args, **kwargs):
    #     pass

    def __init__(self, manufacturer, km=0, **kwargs):
        self.manufacturer = manufacturer
        self.km = km
        self.color_list = None
        for k, v in kwargs.items():
            # setattr(self, k, v)
            self.__setattr__(k, v)

    def __str__(self):
        return " | ".join(
                map(lambda a: f"{a}:{str(self.__getattribute__(a))}",
                    filter(lambda a: not a.startswith('__'), self.__dir__())))

        # return f"Vehicle: {self.manufacturer} | {self.km}"

    def __repr__(self):
        return self.manufacturer

    def __eq__(self, other: 'Vehicle'):
        return self.manufacturer == other.manufacturer and \
            self.km == other.km




if __name__ == '__main__':
    v = Vehicle('mazda')
    # print(v.manufacturer)
    v.temp = 4
    # print(v.temp)
    v1 = Vehicle('toyota', color='white', model='yaris')
    # print(v1.model)
    # print(v1)
    l = [v, v1]
    # print(l)
    # print(v.__dict__)
    v2 = Vehicle('toyota')
    v3 = Vehicle('toyota')
    print(v3 == v2)
    print(v3 != v2)

