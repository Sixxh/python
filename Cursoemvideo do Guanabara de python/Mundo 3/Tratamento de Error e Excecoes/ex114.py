import requests
    
site = 'https://www.google.com'
print(site)
r = requests.get(site)
if r.status_code != 200:
    print('nah')
else:
    print('did it')