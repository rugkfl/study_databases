def mongo_connect(colname):
    from pymongo import MongoClient    # mongodb에 접속 -> 자원에 대한 class
    mongoClient=MongoClient("mongodb://localhost:27017/")    # database 연결
    database=mongoClient["local"]    # collection 작업
    collection=database[colname]    # insert 작업 진행
    return collection




