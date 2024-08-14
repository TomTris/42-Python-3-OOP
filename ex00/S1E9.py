from abc import ABC, abstractmethod


class Character(ABC):
    """My Abstract class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Init first_name required, is_alive by default = True"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Change is_alive to False"""
        self.is_alive = False


class Stark(Character):
    """A Drived Class"""

    def __init__(self, first_name, is_alive=True):
        """Init a Stark"""
        super().__init__(first_name, is_alive)


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    print("-----------------------------")


if __name__ == "__main__":
    main()