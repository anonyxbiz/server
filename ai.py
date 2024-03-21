from requests import get, post
from subprocess import run

p = print

def scrape():
    r = get('https://github.com/anonyxbiz/server.git')

    p(r.status_code)

if __name__ == "__main_":
    from os import system as o
    o('clear')
    scrape()