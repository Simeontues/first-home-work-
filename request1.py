import requests

r = requests.get('https://www.youtube.com/')

print(r.url)
print(r.encoding)
print( r.headers['content-type'])
print(r.status_code)
print(r)
print(dir(r))
print(r.text)