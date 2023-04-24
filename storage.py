from datetime import datetime

class Measure:
    TYPE_GAS = 1
    TYPE_ELECTRO = 0
    TYPE_WATER = 2

    def __init__(self,  type: int, value: int = 0) -> None:
        self.value = int(value)
        self.type = type
        self.date = datetime.now()


class Storage:
    def __init__(self) -> None:
        self.storage = []


    def add_measure(self, measure: Measure):
        self.storage.append(measure)


    def get_last_measure(self) -> Measure:
        return self.storage[-1]
