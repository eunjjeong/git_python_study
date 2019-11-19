def add(a, b):
    return a + b


def mul(a, b):
    return a * b


if __name__ == "__main__":
    print("Hello python")
    print("hi pycharm")
    x = 10
    y = 5
    print("add({}, {}) = {} \nmul({}, {}) = {}".format(x, y, add(x,y), x, y, mul(x,y)))