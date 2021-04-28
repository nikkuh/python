class Storage:
    in_storage = {'Printers': [], 'Scanners': [], 'Xeroxes': []}

    def receive_items(self, *args):
        for i in args:
            try:
                self.in_storage[i.what_is].append(i)
            except:
                pass

    @property
    def show_storage(self):
        print(f'Storage contains:')
        for i in self.in_storage.keys():
            print(f'\t{i}:')
            for n, j in enumerate(self.in_storage[i], 1):
                print(f'\t\t{n}. {j.tell_name}')

    def return_item(self, Type, number):
        if Type in self.in_storage.keys():
            try:
                item = self.in_storage[f'{Type}'].pop(number - 1)
                return item
            except IndexError:
                print('There is no such index.')
                print(f'Please use the method ".show_storage" for index view.')
            except TypeError:
                print('Index must be a number.')
        else:
            print(f'There is no such equipment.\nThere is only {[key for key in self.in_storage.keys()]}')


class Equipment:
    def __init__(self, name):
        self.name = name

    @property
    def tell_name(self):
        return self.name


class Printer(Equipment):
    def pr(self, text):
        print(text)

    @property
    def what_is(self):
        return 'Printers'


class Scanner(Equipment):
    def sc(self, text):
        self.text = text

    @property
    def what_is(self):
        return 'Scanners'


class Xerox(Equipment):
    def sc(self, text):
        self.text = text

    def pr(self, text):
        print(text)

    def cp(self, text):
        return text

    @property
    def what_is(self):
        return 'Xeroxes'


p1 = Printer('Epson')
p2 = Printer('Epson')
p3 = Printer('Samsung')
p4 = Printer('hp')
s1 = Scanner('hp')
s2 = Scanner('hp')
s3 = Scanner('hp')
x1 = Xerox('Xerox')
x2 = Xerox('Xerox')
item1 = '321'
item2 = False
item3 = {'qwe': [1.2, 4, 5]}

sklad = Storage()
sklad.receive_items(x1, x2, p1, p2, p3, p4, s1, s2, s3, item1, item2, item3)
sklad.return_item('jaja',1)
sklad.return_item('Printers', 'fwe')
new_printer = sklad.return_item('Printers', 10)
sklad.show_storage
new_printer = sklad.return_item('Printers', 3)
new_scanner = sklad.return_item('Scanners', 1)
new_xerox = sklad.return_item('Xeroxes', 2)
new_printer.pr('Hello World!')
sklad.show_storage
