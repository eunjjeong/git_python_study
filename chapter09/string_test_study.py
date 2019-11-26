def string_split():
    coffee_menu = "에스프레소 아메리카노 카페라테 카푸치노"
    print(coffee_menu.split())
    coffee_list = coffee_menu.split()
    [print(coffee) for coffee in coffee_list]
    print()
    coffee_menu2 = "에스프레소,아메리카노,카페라테,카푸치노"
    [print(type(coffee), coffee) for coffee in coffee_menu2.split(',')]
    print()
    coffee_menu3 = "에스프레소\n아메리카노\n카페라테\n카푸치노"
    [print(coffee) for coffee in coffee_menu3.split()]
    print()
    [print(coffee) for coffee in coffee_menu2.split(',',2)]
    print()

def string_strip():
    python_str01 = "  Python  "
    python_str02 = "aaaPython"
    python_str03 = "aaabbPythonbbaaa"
    python_str04 = "aaabbllaaa"
    python_str05 = "\n This is very \n fast. \n\n"
    print(python_str01.strip())
    print(python_str02.strip('a'))
    print(python_str03.strip('ab'))
    print("중간에 공백은 제거 불가능", python_str04.strip('a'))
    print(python_str05.strip())


def string_concat():
    a = " "
    coffee_menu = "에스프레소 아메리카노 카페라테 카푸치노".split()
    join_str = a.join(coffee_menu)
    print(type(join_str), join_str)


def string_find():
    str_f = "Python code Python"
    print("찾는 문자열의 위치 :", str_f.find("python"))
    print("찾는 문자열의 위치 :", str_f.find("code"))
    print("찾는 문자열의 위치 :", str_f.find("python"))

    str_f_se = "Python is powerful. Python is easy to learn"
    print("시작위치와 끝위치 지정 :", str_f_se.find("Python", 10, 30))
    print("시작위치 지정 :", str_f_se.find("Python", 35))

    print("Python의 개수는?", str_f_se.count("Python"))

    print(str_f_se.startswith("P"))
    print(str_f_se.endswith("n"))


def string_replace():
    str_b = '[Python]'
    print("문자열 바꾸기 :", str_b.replace('Python', 'IPython'))
    str_b = str_b.replace('[', '')
    str_b = str_b.replace(']', '')
    print("문자열 바꾸기 :", str_b)


if __name__ == "__main__":
    string_split()
    string_strip()
    string_concat()
    string_find()
    string_replace()