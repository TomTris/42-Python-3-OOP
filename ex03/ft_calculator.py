class calculator:
    def __init__(self, object):
        """Creat an instance of calculator"""
        self.value = object

    def __add__(self, object) -> None:
        """add value by object"""
        i = 0
        for nbr in self.value:
            self.value[i] += object
            i += 1
        print(self.value)

    def __mul__(self, object) -> None:
        """multiple value by object"""
        i = 0
        for nbr in self.value:
            self.value[i] *= object
            i += 1
        print(self.value)

    def __sub__(self, object) -> None:
        """subtract value by object"""
        i = 0
        for nbr in self.value:
            self.value[i] -= object
            i += 1
        print(self.value)

    def __truediv__(self, object) -> None:
        """divide value by object"""
        if object == 0:
            print("Error: divided by 0")
            return
        i = 0
        for nbr in self.value:
            self.value[i] /= object
            i += 1
        print(self.value)
