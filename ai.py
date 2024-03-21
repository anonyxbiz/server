from requests import get, post
from subprocess import run
from os import system as o

p = print

def scrape():
    r = get('https://github.com/anonyxbiz/server.git')

    p(r.status_code, r.text)

o('clear')
scrape()