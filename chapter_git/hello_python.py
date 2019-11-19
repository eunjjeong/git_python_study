def add(a, b):
    return a + b


def div(a, b):
    return a / b


if __name__ == "__main__":
    print("Hello python")
    print("hi pycharm")
    x = 10
    y = 5
    print("add({}, {}) = {}\ndiv({}, {}) = {}".format(x, y, add(x,y), x, y, div(x, y)))