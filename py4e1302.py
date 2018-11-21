import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter address: ')

data = urllib.request.urlopen(link)
print ('Retrieving: ', link)
#for data in xml:
info = data.read().decode()
print('Retrieved', len(info), 'characters')

js = json.loads(info)
counts=list()
for u in js['comments']:
    counts.append(u['count'])

print ('Count: ', len(counts))
total = 0
for count in counts:
    total +=int(count)

print ('Sum: ',total)
