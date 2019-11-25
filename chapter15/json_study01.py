import json

python_dict = {
    "이름":"홍길동",
    "나이":25,
    "거주지":"서울",
    "신체정보":{
        "키":175.4,
        "몸무게":71.2
    },
    "취미":[
        "등산",
        "자전거타기",
        "독서"
    ]
}

print(type(python_dict), python_dict)

json_data=json.dumps(python_dict)
print(type(json_data), json_data)

json_data = json.dumps(python_dict, indent=4, sort_keys=True, ensure_ascii=False)
print(type(json_data), json_data)

python_dict2 = json.loads(json_data)
print(type(python_dict2), python_dict2)

