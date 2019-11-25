def print_name(name):
    if bool(name):
        print("입력된 이름:", name)
    else:
        print("입력된 이름이 없습니다.")


def print_list(list):
    for i in range(len(list)):
        print(i**2)


if __name__ == "__main__":
    res = (lambda x: x**2)(3)

    mySquare = lambda x: x**2
    print(mySquare(9))

    print(res)
    print_name("James")
    print_name("")
    print_name(None)

    myNum=[10,5,12,0,3.5,99.5,42]
    print([min(myNum), max(myNum)])

    myStr='zxyabcd'
    print([min(myStr), max(myStr)])

    list1 = [1, 2, 3, 4, 5]
    # 1, 4, 9, 16, 25
    # 홀수의 경우만 1, 9, 25

    print_list(list1)

    for i in list1:
        if i%2==1:
            print(i**2, end=' ')

    print()
    [print(i**2, end=' ') for i in list1 if i % 2 == 1]

