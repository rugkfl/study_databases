from pymongo import MongoClient 

# ---------------------------------------------------------------------------

parti = input("Input Your Name: ")
print("ToDo List 중 하나 선택 하세요 !")
col_todo_list = list(todo_list_connect.find({}))
for i in range(len(col_todo_list)) :
    if i<4 :
        print("{}. {}".format(i+1, col_todo_list[i]["title"]), end=" , ")
    else :
        print("{}. {}".format(i+1, col_todo_list[i]["title"]))
num_title = int(input("Title 번호 : "))
input_status = input("Status : ")





