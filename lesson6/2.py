class Road:
    asphalt_mass = 25

    def __init__(self, ln, w, t=5):
        self._length = ln
        self._width = w
        self.thickness = t
        print(f'Эта дорога имеет длину {self._length} м, ширину {self._width} м и толщину асфальта {self.thickness} см.')

    def calc_mass(self):
        mass = (self._length * self._width * self.thickness * Road.asphalt_mass) / 1000
        print(f'На эту дорогу потребуется {mass} тонн асфальта.')


Lenin_street = Road(2000, 10)
Lenin_street.calc_mass()
