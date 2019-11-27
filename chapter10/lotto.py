from collections import Counter

file_name = 'lotto_num.csv'

with open(file_name, 'r') as f:
    header = f.readline()
    headerList = header.split(',')

    lotto1 = []
    lotto2 = []
    lotto3 = []
    lotto4 = []
    lotto5 = []
    lotto6 = []
    lottobonus = []

    for line in f:
        lottoList = line.split(',')

        lotto1.append(int(lottoList[0]))
        lotto2.append(int(lottoList[1]))
        lotto3.append(int(lottoList[2]))
        lotto4.append(int(lottoList[3]))
        lotto5.append(int(lottoList[4]))
        lotto6.append(int(lottoList[5]))
        lottobonus.append(int(lottoList[6]))

    f.close()

    lottosum = lotto1 + lotto2 + lotto3 + lotto4 + lotto6
    count = Counter(lottosum)
    print("=== 당첨번호 : 나온횟수 ===")
    for i, j in count.items():
        print('[ %2s : %3s ]'%(i, j))

    countB = Counter(lottobonus)
    print()
    print("=== 2등보너스당첨번호 : 나온횟수 ===")
    for i, j in countB.items():
        print('[ %2s : %2s ]'%(i, j))






