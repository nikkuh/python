class TrafficLight:
    from time import sleep
    __color = None

    def running(self):
        while True:
            self.__color = 'red'
            print(self.__color)
            self.sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            self.sleep(2)
            self.__color = 'green'
            print(self.__color)
            self.sleep(10)


svetofor = TrafficLight()
svetofor.running()
