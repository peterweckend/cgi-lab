#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os
from templates import login_page, after_login_incorrect, secret_page
from secret import username, password

form = cgi.FieldStorage()
f_username = form.getfirst("username")
f_password = form.getfirst("password")

request_type = os.environ.get("REQUEST_METHOD", "GET")
cookie_string = os.environ.get("HTTP_COOKIE")
print("Content-Type: text/html")

c_username = None
c_password = None

cookie_kvs = cookie_string.split("; ")
for cookie_kv in cookie_kvs:
    k, v = cookie_kv.split('=')
    if k == "username":
        c_username = v
    if k == "password":
        c_password = v

if c_username and c_password:
    print()
    print(secret_page(c_username, c_password))

# render the login form
elif request_type == "POST":
    if f_username == username and f_password == password:
        # LOGIN OK, SET COOKIE
        print("Set-Cookie: username={};".format(f_username))
        print("Set-Cookie: password={};".format(f_password))
        print()
        print(secret_page(f_username, f_password))
        print(cookie_string)
    else:
        print()
        print(after_login_incorrect())
else:
    print(login_page())

# print(username, password)