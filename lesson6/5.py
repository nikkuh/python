class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет.')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует мягко и красиво.')


class Handle(Stationery):
    def draw(self):
        print('Маркер самый жирный.')


pen_1 = Pen('Parker')
futuristic_device = Stationery('JQW-20000')
handle_1 = Handle('ErichKrause')
pencil_1 = Pencil('Самоцвет')

pen_1.draw()
pencil_1.draw()
handle_1.draw()
futuristic_device.draw()

print(futuristic_device.title)
