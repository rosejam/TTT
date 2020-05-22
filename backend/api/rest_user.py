from django.http import HttpResponse
import json
 
from api.MongoDBManager import usersManager
 

 
def specific_user( request, email):
    def get():
        dbUserData = usersManager().get_users_from_collection( {'_id': email})
        responseData = dbUserData[0] 
        return HttpResponse( json.dumps( responseData), status=200)
 
    def delete():
        result=usersManager().delete_user_on_collection({'_id':email})
        return HttpResponse(status=204) if result else HttpResponse(status=500)

    def put():
        print(request.body)
        dump_json_data=json.dumps(request.body)
        print(dump_json_data)
        received_json_data=json.loads(dump_json_data)
        print(received_json_data)
        result = usersManager().update_user_on_collection(received_json_data)
        return HttpResponse(status=201) if result else HttpResponse(status=500)

    if request.method == 'GET':
        return get()
    elif request.method == "DELETE":
        print('delete')
        return delete()
    elif request.method == 'PUT':
        return put()
    else:
        return HttpResponse( status=405)
 
def all_users( request):
    def get():
        dbUserData = usersManager().get_users_from_collection({})
        responseData =[]
        for user in dbUserData:
            responseData.append(user)
        return HttpResponse( json.dumps( responseData), status=200)

    def post():
        print(request.POST)
        dump_json_data=json.dumps(request.POST)
        received_json_data=json.loads(dump_json_data)
        result = usersManager().add_user_on_collection(received_json_data)
        return HttpResponse( status=201) if result else HttpResponse( status=500)
    

 
    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    else:
        return HttpResponse( status=405)
