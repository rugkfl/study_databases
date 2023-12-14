def mongo_connect(address, local, data) :           # mongodb에 접속하기 위한 function
    from pymongo import MongoClient   
    mongoClient = MongoClient(address)     
    database = mongoClient[local]     
    collection = database[data]         
    return collection          # database['local.solvingproblelm]에 데이터를 넣어야 하므로 collection 변수를 return

# 데이터
quiz_list = [
    {
        "question": "Python의 생성자 함수 이름은 무엇인가요?",
        "choices": ["__init__", "__main__", "__str__", "__del__"],
        "answer": "__init__",
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "score": 20
    },
    {
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
        "score": 20
    }
]


def mongo_insert(collection,add_quiz):   # insert 작업 진행을 위한 function
    for i in range(len(add_quiz)) :      # 데이터를 순서대로 하나씩 넣어주기 위한 for문
        collection.insert_one(add_quiz[i])
    return

address = "mongodb://localhost:27017"       # mongo_connect의 parameter 값
local = "local"
data = 'solvingproblem'

quiz_list_connect = mongo_connect(address, local, data)      # mongo_connect 함수 호출
# quiz_list_insert = mongo_insert(quiz_list_connect,quiz_list)      #  mongo_connect 함수 호출

pass
question = quiz_list_connect.find({}, {'_id' : 0, 'question' : 1})
choices = quiz_list_connect.find({}, {'_id' : 0, 'choices' :1})
for i in (question) :
    print(i)
for i in (choices) :
    print(i)