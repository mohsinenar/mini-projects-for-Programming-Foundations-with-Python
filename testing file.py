import urllib.request
 
html = urllib.request.urlopen('http://www.wdylike.appspot.com/?q=sex').read()
print(html)
