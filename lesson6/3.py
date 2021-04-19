class Worker:
    inc_dict = {'wage': 0, 'bonus': 0}
    name = ''
    surname = ''
    position = ''
    _income = inc_dict

    def __init__(self, name, surname, position, wage=100, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.inc_dict['wage'] = wage
        self.inc_dict['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{sum(self._income.values())}')


ivan = Position('Ivan', 'Ivanov', 'Janitor', 200, 50)
ivan.get_full_name()
ivan.get_total_income()
