from measurements import Measure


class Storage:
    def __init__(self) -> None:
        self.storage = []


    def add_measure(self, measure: Measure):
        self.storage.append(measure)


    def get_last_measure(self) -> Measure:
        return self.storage[-1]
