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
        "answer_number": 1,
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "answer_number": 1,
        "score": 20
    },
    {
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "answer_number": 3,
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "answer_number": 3,
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
         "answer_number": 2,
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
# quiz_list_insert = mongo_insert(quiz_list_connect,quiz_list)    #  mongo_connect 함수 호출

pass

# quiz_list에 있는 question/choices/answer/answer_number/score를 각각 list로 선언해주고 추후 db에 엡데이트를 위해 id도 list 선언을 해줌
question_list = []
choices_list = []
answer_list = []
answer_num_list = []
score_list = []
id_list=[]

id = quiz_list_connect.find({}, {'_id' : 1, 'question' : 0})   # db에 id의 value값을 뽑아냄
questions = quiz_list_connect.find({}, {'_id' : 0, 'question' : 1})  #db에 quiz_list의 question의 value값을 뽑아냄
choices = quiz_list_connect.find({}, {'_id' : 0, 'choices' : 1})  #db에 quiz_list의 choices의 value값을 뽑아냄
answer = quiz_list_connect.find({}, {'_id' : 0, 'answer' : 1})   #db에 quiz_list의 answer의 value값을 뽑아냄
answer_num = quiz_list_connect.find({}, {'_id': 0, 'answer_number': 1})   #db에 quiz_list의 answer_number의 value값을 뽑아냄
score = quiz_list_connect.find({}, {'_id': 0, 'score' : 1})    #db에 quiz_list의 value값을 뽑아냄

# 각 value들을 반복문을 통해 해당되는 list에 append 해줌
for question in questions :
        question_list.append(question)
for choice in choices :
        choices_list.append(choice)
for answers in answer :
        answer_list.append(answers) 
for answer_number in answer_num :
     answer_num_list.append(answer_number)
for scores in score :
        score_list.append(scores)
for ids in id :
    id_list.append(ids)



class Quiz :
    def __init__(self, question_list, choices_list) :
        self.question_list = question_list
        self.choices_list = choices_list
        self.correct_list = [1, 1, 3, 3, 2]
        self.answers_list = []
        self.get_input=None

    def print_question(self) :
        for i in range(len(question_list)):
            print(question_list[i])
            print(choices_list[i])
            self.get_input = int(input("answer : "))
            self.answers_list.append(self.get_input)
            if self.get_input == self.correct_list[i] :
                 print("정답입니다.")
            else :
                 print("틀렸습니다.")
            
        print("입력한 문항 별 답 : {}".format(self.answers_list))
        return 
    
    def insert_db(self,database,quiz_list) :
        for i, main in enumerate(quiz_list) :
            database.update_many({'_id' : main['_id']}, {'$set' : {'User_answer' : self.answers_list[i]}})
        return
         
quiz = Quiz(question_list, choices_list)  # Quiz 클래스의 인스턴스 생성
quiz.print_question()    # quiz.print_qustion()
quiz.insert_db(quiz_list_connect,id_list)


          