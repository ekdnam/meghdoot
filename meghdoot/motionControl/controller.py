import easytello

# PID
# imutils -> threading


class Controller:
    def __init__(self, tello_ip: str = "192.168.10.1", debug: bool = True):
        self.__tello = easytello.Tello(tello_ip, debug)

    def takeoff(self):
        self.__tello.takeoff()

    def land(self):
        self.__tello.land()

    def streamon(self):
        self.__tello.streamon()

    def streamoff(self):
        self.__tello.streamoff()

    def go_up(self, dist: int):
        self.__tello.up(dist)

    def go_down(self, dist: int):
        self.__tello.down(dist)

    def go_right(self, dist: int):
        self.__tello.right(dist)

    def go_left(self, dist: int):
        self.__tello.left(dist)
