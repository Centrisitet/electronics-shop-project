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
    def item_name(self):
        return self.__name

    @item_name.setter
    def item_name(self, name):
        if len(name) < 10:
            self.__name = name

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                if row[0] != 'name':
                    name, price, quantity = row[0], row[1], row[2]
                    cls.all.append(cls(name, price, quantity))




    @staticmethod
    def string_to_number(string: str):
        num = float(string)
        num = int(num)
        return num
