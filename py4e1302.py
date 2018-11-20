import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter address: ')

json = urllib.request.urlopen(link)
print ('Retrieving: ', link)
#for data in xml:
data = json.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)

counts = tree.findall('.//count')
print ('Count: ', len(counts))
total = 0
for count in counts:
    total +=int(count.text)

print ('Sum: ',total)
