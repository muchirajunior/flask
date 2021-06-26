API authorization decorators
--------------------------------

the decorators allow api users to pass authorization keys 
on header request headers

for any request without the authorization key is denied
this  enhances API security

the codes are separate

on app.py there is a common decorator using app secret key for authorization

the auth.py builds a decorator that stores data in TinyDB database 
which stores in json format in this case data.json
The data searches user in tiny db and authorizes for access
the implementetion is on the mypage route.

