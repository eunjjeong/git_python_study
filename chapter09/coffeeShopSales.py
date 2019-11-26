if __name__ == "__main__":
    file_name = 'coffeeShopSales.txt'
    with open(file_name, 'r') as f:
        for line in f:
            print(line, end='')

    with open(file_name, 'r') as f:
        header = f.readline()
        headerList = header.split()

        espresso = []
        americano = []
        cafelatte = []
        cappucino = []

        for line in f:
            dataList = line.split()

            espresso.append(int(dataList[1]))
            americano.append(int(dataList[2]))
            cafelatte.append(int(dataList[3]))
            cappucino.append(int(dataList[4]))

        f.close()

        print("{0}: {1}".format(headerList[1], espresso))
        print("{0}: {1}".format(headerList[2], americano))
        print("{0}: {1}".format(headerList[3], cafelatte))
        print("{0}: {1}".format(headerList[4], cappucino))

        total_sum = [sum(espresso), sum(americano), sum(cafelatte), sum(cappucino)]
        total_mean = [sum(espresso)/len(espresso), sum(americano)/len(americano),
                      sum(cafelatte)/len(cafelatte), sum(cappucino)/len(cappucino)]

        for k in range(len(total_sum)):
            print('[{0}] 판매량'.format(headerList[k+1]))
            print('-나흘 전체: {0}, 하루 평균: {1}'.format(total_sum[k], total_sum[k]))

    with open(file_name, 'r') as f:
        header = f.readline()
        print(header, header.split())
        coffee_list = []
        [coffee_list.append(line.split()) for line in f]

    # dictionary로
    with open(file_name, 'r') as f:
        header = f.readline()
        header_list = header.split()
        for line in f:
            data_list = line.split()
            data_list2 = dict(zip(header_list, data_list))
            print(data_list2)

