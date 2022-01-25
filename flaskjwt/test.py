# type:ignore
import requests

def getToken():
    payload={
        "username":"muchirajunior",
        "password":"junior&1234"
    }
    result= requests.post("http://localhost:5000/login",json=payload)

    return result.json()['access_token']

def testToken(token):
    header={
        "Authorization":"Bearer "+token
    }
    result= requests.get("http://localhost:5000/user", headers=header)
    print(result.json())
    

testToken(getToken())