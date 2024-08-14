from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, name, is_alive=True):
        """Init a King"""
        super().__init__(name, is_alive)

    def set_eyes(self, new: str):
        """Set eyes color to new"""
        self.eyes = new

    def set_hairs(self, new: str):
        """Set hair color to new"""
        self.hairs = new

    def get_eyes(self):
        """return current eyes color"""
        return self.eyes

    def get_hairs(self):
        """return current hair color"""
        return self.hairs

def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
