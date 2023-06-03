import csv



class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quant = quantity
        Item.all.append(self)

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, item_name: str):
        if len(item_name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = item_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        full_price = self.price * self.quant
        return full_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quant})"

    def __str__(self):
        return f"{self.__name}"

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('../src/items.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != 'name':
                    __name, price, quantity = row[0], row[1], row[2]
                    cls(__name, price, quantity)

    @staticmethod
    def string_to_number(string: str):
        num = float(string)
        num = int(num)
        return num

    def __add__(self, other):
        return self.quant + other.quant

