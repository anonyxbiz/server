from requests import get, post
from subprocess import run

p = print

r = get('https://github.com/anonyxbiz/server.git')

p(r.status_code)

run('git pull origin main')