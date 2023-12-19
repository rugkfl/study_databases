def mongo_connect(data) :           # mongodb에 접속하기 위한 function
    from pymongo import MongoClient   
    mongoClient = MongoClient("mongodb://localhost:27017")     
    database = mongoClient["local"]     
    collection = database[data]         
    return collection          # database['local.solvingproblelm]에 데이터를 넣어야 하므로 collection 변수를 return

todo_list = [
    {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
    {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
    {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
    {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의o 계획서를 검토하고 필요한 부분을 수정합니다."},
    {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."} ]

# todo_list insert
def mongo_insert(collection,add_todo):   # insert 작업 진행을 위한 function
    for i in range(len(add_todo)) :      # 데이터를 순서대로 하나씩 넣어주기 위한 for문
        collection.insert_one(add_todo[i])
    return

todo_list_connect = mongo_connect('todos_list') 
# quiz_list_insert = mongo_insert(todo_list_connect, todo_list)    #  mongo_connect 함수 호출


user_name_list = [] # 참여자에 대한 list

get_name_list=[] 

parti_todos_list = []



# user_todos = mongo_insert(mongo_connect('participants_todos'), parti_todos_list)

# ---------------------------------------------------------------------------

   
while True:  # 전체 loop
    parti = input("Input Your Name: ") # 참여자 입력
    dic_parti= {}   # 참여자의 dictionary
    dic_parti["참여자"] = parti     #db에 '참여자'라는 key 값을 생성하고 parti 값을 value로 넣음
    user_name_list.append(dic_parti)    #user_name_list에 dic_parti안에 있는 key값과 value를 append하여 넣어줌
    participants = mongo_connect('participants')  # participants collection에 연결
    user_list = mongo_insert(participants,user_name_list)

    while True :
        col_todo_list = list(todo_list_connect.find({}))  # todos_list collection에서 전체 내용 find
        for i in range(len(col_todo_list)) : # 그 중 title 값만 가져오기 위한 for문
                if i<4 :
                    print("{}. {}".format(i+1, col_todo_list[i]["title"]), end=" , ")
                else :
                    print("{}. {}".format(i+1, col_todo_list[i]["title"]))
        num_title = int(input("Title 번호 : "))  #  title 번호 입력 
        participants_connect = mongo_connect('participants') # participants collection에 연결
        col_parti_list = list(participants_connect.find({})) # participants collection의 전체 내용 find(참여자와 각각의 _id)

        for i in range(len(col_parti_list)): 
             get_name_list.append(col_parti_list[i]["참여자"])
             pass
        
        for i in range(len(get_name_list)):
            if parti == get_name_list[i]:
                somthing_id = col_parti_list[i]['_id']
                break

        # find parti id와 이름 (참여자 이름값만 정제) v
        # 입력한 값이랑 참여자 이름값 비교해서 맞는 주소? 맞는값 v
        # 그 _id값을 어딘가의 변수에 저장한다. v
        # 그 변수를 dic_num에 연결한다.
        input_status = input("Status : ")
        
        # participants_todos collection에 올리기 위한 dictionary
        dic_num=[{
             '_id' : somthing_id,
             'Title' : num_title,
             'Status' : input_status
        }]

        participants_todos_connect = mongo_connect('participants_todos') # participants_todos collection에 연결
        update_todos = mongo_insert(participants_todos_connect,dic_num) #아 몰랑
        
        # 종료 여부에 대한 반복문
        while True:
            str_input = input("종료 여부 : ")
            if str_input == "c" or str_input == "q" or str_input =="x":
                break
            else:
                pass
        if str_input == "c":
                continue   # 'c' 입력 시 ToDo list를 다시 출력하도록 루프의 처음으로 돌아감
        elif str_input == 'q' :
            print("------------------")
            break   # 'q' 입력 시 사용자 이름을 다시 입력받도록 루프를 빠져나감
        elif str_input =="x":
            print("------------------")
            print("프로그램이 종료되었습니다.")
            exit()  # 'x' 입력 시 프로그램 종료
    if str_input == 'q': 
         continue  # 사용자 이름을 다시 입력받도록 루프의 처음으로 돌아감
    
# pass: pass는 아무것도 하지 않는다는 것을 나타내는 키워드입니다. 주로 코드의 형태를 유지하거나 나중에 작성할 코드를 표시하는데 사용
# break: break는 현재의 반복문을 즉시 종료하고, 제어 흐름을 반복문 바로 다음의 문장으로 이동시키는 키워드입니다. break는 주로 무한루프에서 특정 조건을 만족하면 루프를 빠져나가기 위해 사용
# continue: continue는 현재의 반복을 즉시 종료하고, 제어 흐름을 반복문의 시작 부분으로 돌려보내는 키워드입니다. continue는 주로 반복문 내에서 특정 조건을 만족하는 경우 나머지 코드를 건너뛰고 다음 반복을 시작하기 위해 사용
