from requests import get, post

p = print
r = get('https://github.com/anonyxbiz/server.git')

p(r.status_code)
