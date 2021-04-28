class Date:
    string_date = None

    def __init__(self, date):
        if Date.checker(date):
            self.string_date = date

    @classmethod
    def to_int(cls, string_date):
        try:
            day, month, year = map(int, string_date.split('-'))
            return day, month, year
        except ValueError:
            print('Введен неверный формат даты.')

    @staticmethod
    def checker(string):
        try:
            d, m = Date.to_int(string)[:2]
            if d in range(1, 32) and m in range(1, 13):
                return True
        except TypeError:
            return False
        return False


print(Date.checker('31-10-2021'))
print(Date.checker('32-02-2430'))
print(Date.to_int('02-08-1991'))
d11 = Date('sj-3r-121f')
d12 = Date('sadi734y')
