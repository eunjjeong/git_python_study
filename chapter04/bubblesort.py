import random as rnd

# 버블정렬
def bubble_sort(random_list):
    for i in range(0, len(random_list)-1):
        for j in range(0, len(random_list)-1-i):
            if random_list[j] > random_list[j + 1]:
                temp = random_list[j]
                random_list[j] = random_list[j + 1]
                random_list[j + 1] = temp
    return random_list


if __name__ == "__main__":
    random_list = []
    rnd.seed(1) # 랜덤한 숫자 고정
    for num in range(0, 10):
        random_list.append(rnd.randint(1, 46))
    print("정렬전 : {}".format(random_list))

    sortedList = bubble_sort(random_list)
    print("정렬후 : {}".format(sortedList))