import numpy as np
# 1번문제
import re

file_name = 'Gettysburg_Address.txt'
dictionary = []
w_word = 0
w_cnt = 1
def check(dictionary, target):
    if target != None:
        target = re.sub('[^A-Za-z0-9]+', '', target) # 마침표 쉼표 -기호 제외 시킴

    if target == None or target == '':
        return

    found = False

    for word in dictionary:
        if word[w_word]==target:
            word[w_cnt]=word[w_cnt]+1
            found = True
            break

    if not found:
        word=[{} for x in range(max(w_word, w_cnt)+1)]
        word[w_word]=target
        word[w_cnt]=1
        dictionary.append(word) # 못찾으면 단어랑 빈도수 추가

def gettysburg():
    f = open(file_name, 'r')
    while True:
        line = f.readline()
        if not line: break

        splits = line.split(" ")
        for split in splits:
            check(dictionary, split)
    f.close()

    dictionary.sort(key=lambda a:(a[w_cnt]), reverse = True)

    print("빈도순으로 정렬")
    for word in dictionary:
        if word[w_cnt] > 2:
            print("%s : %d"%(word[w_word], word[w_cnt]))


# 3번문제
def tree_koong():
    tree = 0
    while tree < 10:
        tree = tree + 1
        print("나무꾼이 나무를 %2s번 찍습니다"%tree)
    print("나무가 넘어갑니다")

# array, commands commands = [[2,5,3],[4,4,1],[1,7,3]]

# 4번문제
def bubble_sort(random_list):
    for i in range(0, len(random_list)-1):
        for j in range(0, len(random_list)-1-i):
            if random_list[j] > random_list[j + 1]:
                temp = random_list[j]
                random_list[j] = random_list[j + 1]
                random_list[j + 1] = temp
    return random_list


def solution(array, commands):
    print("=========solution.py=========")
    answer = []
    for i in range(len(commands)):
        if commands[i][0] == 1:
            cut_array = array[(commands[i][0] - 1):commands[i][1]]
            sort_array = bubble_sort(list(cut_array))
            result_num = sort_array[(commands[i][2] - 1)]
            print("{}를 {}번째부터 {}번째까지 자릅니다.{}의 {}째 숫자는 {}입니다.".format(
                array, commands[i][0], commands[i][1], sort_array, commands[i][2], result_num
            ))
            answer.append(result_num)
        else:
            cut_array = array[(commands[i][0]-1):commands[i][1]]
            sort_array = bubble_sort(list(cut_array))
            result_num = sort_array[(commands[i][2]-1)]
            print("{}를 {}번째부터 {}번째까지 자른 후 정렬합니다.{}의 {}째 숫자는 {}입니다.".format(
                array, commands[i][0], commands[i][1], sort_array, commands[i][2], result_num
            ))
            answer.append(result_num)

    print("answer : {}".format(answer))
    return answer


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    array = np.array(array)
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    solution(array, commands)

    #gettysburg()
    #tree_koong()
    # lambdaAdd = lambda x, y: x + y
    # lambdaMinues = lambda x, y: x - y
    # lambdaMul = lambda x, y: x * y
    # lambdaDiv = lambda x, y: x / y
    # print("==========사칙연산==========")
    # print("더하기 : {}".format(lambdaAdd(2,3)))
    # print("빼기 : {}".format(lambdaMinues(5,3)))
    # print("곱하기 : {}".format(lambdaMul(6,7)))
    # print("나누기 : {}".format(lambdaDiv(10,2)))
