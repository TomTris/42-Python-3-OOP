from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, is_alive=True):
        """init Baratheon"""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'


class Lannister(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, is_alive=True):
        """init Lannister"""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(cls, name, is_alive=True):
        """Create an instance"""
        return (cls(name, is_alive))


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    a = f"Name : {Jaine.first_name, type(Jaine).__name__}"
    a += f", Alive : {Jaine.is_alive}"
    print(a)


if __name__ == "__main__":
    main()
