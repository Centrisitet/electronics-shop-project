from src.item import Item


class MixinLanguage:
    def __init__(self):
        self.language == 'EN'
        
    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'


class Keyboard(Item, MixinLanguage):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return f'{self.__language}'

    def __repr__(self):
        return f'Keyboard{self.name}, {self.price}, {self.quant}'




