'''
JSON encoding : python → JSON
JSON decoding : JSON → python
'''
import json

# dict형 선언
user = {
    "id" : "gildong",
    "password" : "192837",
    "age" : 30,
    "hobby" : ["football", "programming"]
}

# encoding, indent = 4 : 띄어쓰기 4칸
json_data = json.dumps(user, indent = 4)
print(json_data)
'''
{
    "id": "gildong",
    "password": "192837",
    "age": 30,
    "hobby": [
        "football",
        "programming"
    ]
}
'''

# decoding
data = json.loads(json_data)
print(data)

'''
{'id': 'gildong', 'password': '192837', 'age': 30, 'hobby': ['football', 'programming']}
'''

# user 객체를 json file "user.json"에 dump 생성
with open("./book/part03/appendix/user.json", 'w', encoding="utf-8") as file:
    json.dump(user, file, indent = 4)