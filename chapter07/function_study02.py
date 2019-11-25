"""
list tuple dictionary set 에서 하나를 선택하여 아래 프로그램을 작성하시오.
--> dictionary, 하나
student_management 패키지를 추가
학생정보는 : 학생번호, 학생명, 국어, 영어, 수학
출력결과 : 1, 김승영, 90, 90, 90, 270, 90.0

1. 학생목록 2. 학생추가 3. 학생수정 4. 학생삭제 5. 종료 메뉴 추가
2. 프로그램 수행시 먼저 student_list.txt 파일을 읽어와 수행
3. 각각 메뉴별 수행되도록 작성
4. 종료시 학생목록이 student_list.txt에 저장
"""

# 학생 리스트 불러오기
student_list=[]
def read_student():
    global student_list
    try:
        fp=open('student_list.txt', 'r')
        for line in fp.readlines():
            student_list.append(line.split())
    except FileNotFoundError as FNF:
        print("파일이 존재하지 않습니다.", FNF, sep='\n')
    finally:
        fp.close()


# 학생목록보여주는함수
def main_student_list():
    global student_list
    print("%20s"%("<학생목록>"))
    print("학생번호 학생이름 국어성적 영어성적 수학성적 총합 평균")
    for i in range(len(student_list)):
        total = int(student_list[i][2]) + int(student_list[i][3]) + int(student_list[i][4])
        avg = total/3
        print("%3s %7s %5s %6s %7s %5d %0.1f"%(student_list[i][0], student_list[i][1], student_list[i][2], student_list[i][3], student_list[i][4], total, avg))


# 학생추가함수
def add_student():
    global student_list

    while 1:
        sign = 0
        id=input("추가할 학생번호를 입력하세요(종료:0) : ")
        for j in range(len(student_list)):
            if student_list[j][0] == id:
                print("존재하는 학생번호 입니다.")
                sign = 1
            if sign == 0: break
            return
        if id == '0': return
        name=input("추가할 학생이름을 입력하세요(종료:0) : ")
        if name == '0': return
        kor=input("추가할 학생의 국어성적을 입력하세요(종료:0) : ")
        if okscore(int(kor)) == 0:
            print("0~100사이의 점수를 입력해주세요.")
            return
        if kor == '0': return
        eng=input("추가할 학생의 영어성적을 입력하세요(종료:0) : ")
        if okscore(int(eng)) == 0:
            print("0~100사이의 점수를 입력해주세요.")
            return
        if eng == '0': return
        math=input("추가할 학생의 수학성적을 입력하세요(종료:0) : ")
        if okscore(int(math)) == 0:
            print("0~100사이의 점수를 입력해주세요.")
            return
        if math == '0': return
        student_list.append([id, name, kor, eng, math])
        print("%s 학생이 추가되었습니다."%name)


# 학생수정함수
def modify_student():
    global student_list
    modify_list_student()
    while 1:
        sign = 0
        id = input("수정할 학생번호를 입력하세요(종료:0) : ")
        for i in range(len(student_list)):
            if student_list[i][0] == id:
                m = i
                sign = 1
        if sign == 1: break
        print("없는 학생번호 입니다.")
        if id == '0': return
    while 1:
        modify_list_student2(m)
        a = input("========STUDENT MODIFY========\n       1.학생이름 수정\n       2.국어점수 수정\n       3.영어점수 수정\n       4.수학점수 수정\n       5.다른학생으로 변경\n       6.종료\n==============================\n => 원하는 메뉴 번호를 선택하세요 : ")
        if a == "1":
            name = input("수정할 학생이름을 입력하세요(종료:0) : ")
            if name == '0': return
            student_list[m][1] = name
            print("이름 수정완료")
            continue
        elif a == "2":
            kor = input("수정할 국어점수를 입력하세요(종료:0) : ")
            if okscore(int(kor)) == 0:
                print("0~100사이의 점수를 입력해주세요.")
                return
            if kor == '0': return
            student_list[m][2] = kor
            print("국어점수 수정완료")
            continue
        elif a == "3":
            eng = input("수정할 영어점수를 입력하세요(종료:0) : ")
            if okscore(int(eng)) == 0:
                print("0~100사이의 점수를 입력해주세요.")
                return
            if eng == '0': return
            student_list[m][3] = eng
            print("영어점수 수정완료")
            continue
        elif a == "4":
            math = input("수정할 수학점수를 입력하세요(종료:0) : ")
            if okscore(int(math)) == 0:
                print("0~100사이의 점수를 입력해주세요.")
                return
            if math == '0': return
            student_list[m][4] = math
            print("수학점수 수정완료")
            continue
        elif a == "5":
            modify_student()
            return
        elif a == "6":
            return
        else:
            continue


# 학생수정전 학생 전체목록 보여주는 함수
def modify_list_student():
    global student_list
    print("학생번호 학생이름 국어성적 영어성적 수학성적")
    for i in range(len(student_list)):
        print("%3s %7s %5s %6s %7s"% (student_list[i][0], student_list[i][1], student_list[i][2], student_list[i][3],student_list[i][4]))


# 선택한 학생 보여주는 함수(수정)
def modify_list_student2(i):
    global student_list
    print("학생번호 학생이름 국어성적 영어성적 수학성적")
    print("%3s %7s %5s %6s %7s"% (student_list[i][0], student_list[i][1], student_list[i][2], student_list[i][3],student_list[i][4]))


# 학생 삭제 함수
def delete_student():
    global student_list
    main_student_list()
    while 1:
        sign = 0
        id = input("삭제할 학생번호를 입력하세요(종료:0) : ")
        for i in range(len(student_list)):
            if student_list[i][0] == id:
                m = i
                sign = 1
        if sign == 1: break
        print("존재하지않는 번호입니다.")
        if id == '0': return
    print("%s 학생이 삭제되었습니다."%student_list[m][1])
    student_list.remove(student_list[m])


# 종료 및 저장함수
def save_exit():
    global student_list
    try:
        fp = open("student_list.txt", "w")
        for i in range(len(student_list)):
            fp.write(student_list[i][0] + ' ' + student_list[i][1] + ' ' + student_list[i][2] + ' ' + student_list[i][3] + ' ' + student_list[i][4] + '\n')
    except FileNotFoundError as FNF:
        print("파일이 존재하지 않습니다.", FNF, sep='\n')
    finally:
        fp.close()


# 0~100 사이의 점수를 입력했는지 확인하는 함수
def okscore(num):
    return (num >= 0) and (num <= 100)


# 메인메뉴 함수
def main():
    while 1:
        i = input("========STUDENT MENU========\n         1.학생목록\n         2.학생추가\n         3.학생정보수정\n         4.학생삭제\n         5.종료\n=============================\n => 원하는 메뉴 번호를 선택하세요 : ")
        if i == "1":
            main_student_list()
            continue
        elif i == "2":
            add_student()
            continue
        elif i == "3":
            modify_student()
            continue
        elif i == "4":
            delete_student()
            continue
        elif i == "5":
            save_exit()
            return
        else: continue


if __name__ == "__main__":
    read_student()
    main()
