from src.item import Item


class MixinLanguage:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = 'EN'

    @property
    def language(self):
        return f'{self.__language}'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f'Keyboard{self.name}, {self.price}, {self.quant}'




