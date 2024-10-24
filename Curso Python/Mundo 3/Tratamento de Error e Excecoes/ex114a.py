import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com')
except:
    print('deu erro')
else:
    print('Tudo certo')