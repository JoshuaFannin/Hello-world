import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter address: ')
counts= list()
tree = list()
xml = urllib.request.urlopen(link)
print ('Retrieving: ', link)
#for data in xml:
data = xml.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print ('Count: ', len(counts))
total = 0
for count in counts:
    total +=int(count.text)

print ('Sum: ',total)
