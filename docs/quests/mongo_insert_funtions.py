


def mongo_connect() :           # mongodb에 접속하기 위한 function
    from pymongo import MongoClient   
    mongoClient = MongoClient("mongodb://localhost:27017")     
    database = mongoClient["local"]     
    collection = database['fruits']         
    return collection          # database['fruits']에 데이터를 넣어야 하므로 collection 변수를 return

# 데이터
fruits_info = [
    {"name": "사과", "color": "빨강", "origin": "한국"},
    {"name": "바나나", "color": "노랑", "origin": "필리핀"},
    {"name": "포도", "color": "보라", "origin": "칠레"},
    {"name": "오렌지", "color": "주황", "origin": "미국"},
]

def mongo_insert(collection,add_fruits):   # insert 작업 진행을 위한 function
    for i in range(len(add_fruits)) :      # 데이터를 순서대로 하나씩 넣어주기 위한 for문
        collection.insert_one(add_fruits[i])
    return
fruits_connect = mongo_connect()      # mongo_connect 함수 호출
fruits_insert = mongo_insert(fruits_connect,fruits_info)      #  mongo_connect 함수 호출

pass