from src.item import Item


class Keyboard(Item):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def change_lang(self) -> None:
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return f'{self.__language}'

    def __repr__(self):
        return f'Keyboard{self.name}, {self.price}, {self.quant}'




