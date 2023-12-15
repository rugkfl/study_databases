def mongo_connect(address, local, data) :           # mongodb에 접속하기 위한 function
    from pymongo import MongoClient   
    mongoClient = MongoClient(address)     
    database = mongoClient[local]     
    collection = database[data]         
    return collection          # database['local.solvingproblelm]에 데이터를 넣어야 하므로 collection 변수를 return

todo_list = [
    {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
    {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
    {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
    {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
    {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."} ]

def mongo_insert(collection,add_todo):   # insert 작업 진행을 위한 function
    for i in range(len(add_todo)) :      # 데이터를 순서대로 하나씩 넣어주기 위한 for문
        collection.insert_one(add_todo[i])
    return

address = "mongodb://localhost:27017"       # mongo_connect의 parameter 값
local = "local"
data = 'todos_list'

todo_list_connect = mongo_connect(address, local, data)      # mongo_connect 함수 호출
# quiz_list_insert = mongo_insert(todo_list_connect, todo_list)    #  mongo_connect 함수 호출

title_list = []
description_list = []
id_list = []


id = todo_list_connect.find({}, {'_id' : 1, 'title': 0})
titles = todo_list_connect.find({}, {'_id': 0, 'title': 1})
descriptions = todo_list_connect.find({}, {'_id': 0, 'description': 1 })

for title in titles :
    title_list.append(title)
for description in descriptions :
    description_list.append(description)
for ids in id_list :
    id_list.append(ids)


input_name =""

input_name = input("Input Your Name: ")
if input_name == '참여자 1' :
    print("ToDo List 중 하나 선택 하세요 !")
    print
    
    
