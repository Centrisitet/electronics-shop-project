from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quant}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return int(self.__number_of_sim)

    @number_of_sim.setter
    def number_of_sim(self, number: int):
        if number < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__number_of_sim == number

    def __add__(self, other):
        if isinstance(self, Item) and isinstance(other, Phone):
            return self.quant + other.quant
        else:
            return 'Error'

