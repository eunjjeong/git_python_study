class Bicycle():

    # __ => private 밖에서 보이지 않게 ( shift + f6 : 전체바꾸기 )
    def __init__(self, wheel_size=10, color="white"):
        self.wheel_size = wheel_size
        self.color = color

    def move(self, speed):
        print("자전거: 시속{}킬로미터로 전진".format(speed))

    def turn(self, direction):
        print("자전거: {}회전".format(direction))

    def stop(self):
        print("자전거({}, {})): 정지".format(self.wheel_size, self.color))

    # ALT + INSERT
    def __str__(self) -> str:
        return str("자전거({}, {})".format(self.wheel_size, self.color))


class Car(Bicycle):
    def stop(self):
        print("자동차({}, {})): 정지".format(self.wheel_size, self.color))


if __name__ == "__main__":
    my_bicycle = Bicycle()

    my_bicycle2 = Bicycle(30, 'black')

    [print(c) for c in [my_bicycle, my_bicycle2]]

    print(my_bicycle.wheel_size)