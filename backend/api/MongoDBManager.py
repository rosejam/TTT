import pymongo
 
class usersManager:
    _instance = None
    client=pymongo.MongoClient("mongodb://root:ssafy@127.0.0.1:27017")
    database = client['TTT']['users']
 
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
 
    def get_users_from_collection(cls, _query):
        assert cls.database
        return cls.database.find( _query)
 
    def add_user_on_collection(cls, _data):
        if type( _data) is list:
            return cls.database.insert_many( _data)
        else :
            return cls.database.insert_one( _data)