
from solvingProblem_funtions import Quiz, mongo_connect

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


quiz = Quiz(question_list, choices_list)  # Quiz 클래스의 인스턴스 생성
quiz.print_question()    # quiz.print_qustion()
quiz.insert_db(quiz_list_connect,id_list)