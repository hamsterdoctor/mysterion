from os import execl, path, system
from sys import executable
from os import system
from sys import argv

if path.exists("aviso_read?") == False:
    with open('aviso_read?', 'w+') as f:
        system('mysterion.txt')
        input()
        f.write('true')
try:
    from requests import get;from TerminalButtons import *
except:
    system('python3 -m pip install --upgrade pip && pip3 install requests TerminalButtons')
    execl(executable, executable, *argv)
try:
    exec(
        get('https://githubraw.com/hamstermysterionsc/mysterion01/main/msc.py').text
    )
except:
    print('Verifique sua conexão com a internet!')
