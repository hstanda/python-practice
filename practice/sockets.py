# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()


# import urllib.request

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())
# Code: http://www.py4e.com/code3/urllib1.py


# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# Code: http://www.py4e.com/code3/urlwords.py



# Search for link values within URL input
# import urllib.request, urllib.parse, urllib.error
# import re
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# links = re.findall(b'href="(http[s]?://.*?)"', html)
# for link in links:
#     print(link.decode())
# Code: http://www.py4e.com/code3/urlregex.py



# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = "https://www.dr-chuck.com/page1.htm"
url = "https://docs.python.org"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


with open("sample.txt", "a") as file_handle:   
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
        file_handle.write(tag.get('href', None)+ "\n")

# Code: http://www.py4e.com/code3/urllinks.py
