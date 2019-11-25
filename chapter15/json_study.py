import json

student = [
    {
        "no":1,
        "name":"김승영",
        "score":{"국어":90, "영어":90, "수학":90}
    },
    {
        "no":2,
        "name":"지재삼",
        "score":{"국어":80, "영어":79, "수학":69}
    }
]

print(type(student)) #dictionary

# write
json_student = json.dumps(student, ensure_ascii=False)
print(type(json_student))

with open('json_test.txt', 'w', encoding='utf-8') as f:
    json.dump(json_student, f, ensure_ascii=False) # json 파일 작성 한글은 unicode 형태로 저장

# read
with open('json_test.txt', 'r', encoding='utf-8') as f: # json 형태의 파일 load
    x = json.load(f)
    print(type(x), x)

students = json.loads(x)
type(students)

for std in students:
    print("{} {} #{} {} {}"
          .format(type(std['no']),
                  type(std['name']),
                  type(std['score']['국어']),
                  type(std['score']['영어']),
                  type(std['score']['수학'])))

    print(std['no'], std['name'], end=' ')
    total = sum ([x for x in std['score'].values()])

    [print(score, end=' ') for score in std['score'].values()]
    print(total, total/float(3))




