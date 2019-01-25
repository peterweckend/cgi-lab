#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
from urllib.parse import parse_qs

import json
import os

print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</head>")
print("<h2>Hello World</h2>")

# print query string
qs = os.environ.get("QUERY_STRING", None)
print("<dl>")
print("<dt>QUERY_STRING</dt>")
print("<dd>{}</dd>".format(parse_qs(qs)))
print("<dt>HTTP_USER_AGENT</dt>")
ua = os.environ.get("HTTP_USER_AGENT", None)
print("<dd>{}</dd>".format(ua))
print("</dl>")


# dump env variables
#cgi.print_environ()
# print(os.environ)
print("<pre>")
print(json.dumps(dict(os.environ)))
print("</pre>")
