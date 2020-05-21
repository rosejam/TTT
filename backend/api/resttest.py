from django.http import HttpResponse
import json
 
from api.MongoDBManager import usersManager
 
def specific_user( request, email):
    def get():
        dbUserData = usersManager().get_users_from_collection( {'email': email})
        responseData = dbUserData[0]
        del responseData['_id']
 
        return HttpResponse( json.dumps( responseData), status=200)
 
    def post():
        received_json_data=json.loads(request.POST)
        del received_json_data['_id']
        result = usersManager().add_user_on_collection(received_json_data)
        return HttpResponse( status=201) if result else HttpResponse( status=500)
 
    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    else:
        return HttpResponse( status=405)
 
def all_users( request):
    def get():
        dbUserData = usersManager().get_users_from_collection({})
        responseData = []
        for user in dbUserData:
            del user['_id']
            responseData.append(user)
 
        return HttpResponse( json.dumps( responseData), status=200)
 
    if request.method == 'GET':
        return get()
    else:
        return HttpResponse( status=405)
