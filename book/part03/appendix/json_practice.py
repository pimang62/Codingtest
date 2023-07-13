'''
https://jsonplaceholder.typicode.com/

REST API
- /user/1 : 1명의 사용자 정보
- /users : 모든 사용자 정보

'''
import json
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# 응답(Response) 데이터가 JSON 형식이므로 파이썬 객체로 변환
data = response.json()    # json.loads(response) : str형

# 모든 사용자(user) 정보를 확인하여 이름 정보만 삽입
name_list = []
for user in data:   # dict 형태인 user
    name_list.append(user["name"])   # "name"의 value만 추출

print(name_list)
