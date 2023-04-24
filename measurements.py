from datetime import datetime

class Measure:
    def __init__(self,  type: int, value: int = 0) -> None:
        self.value = int(value)
        self.type = type
        self.date = datetime.now()


class Types:
    TYPE_GAS = 1
    TYPE_ELECTRO = 0
    TYPE_WATER = 2

    @staticmethod
    def get_label(type: int):
        names = {
            Types.TYPE_ELECTRO: 'электроэнергия',
            Types.TYPE_GAS: 'газ',
            Types.TYPE_WATER: 'водоснабжение'
        }
        return names[type]