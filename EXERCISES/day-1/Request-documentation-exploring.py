import requests

r = requests.get("https://api.github.com/events")


payload = {"a":1 , "b":2}

r = requests.get("https://api.github.com/events", params=payload)
print(r.url)
#print(r.text)
print(r.encoding)
print(r.json)
print(r.status_code)



#r.encoding = "ISO-8859-1"
#print(r.encoding)

#print(r.content)

#convert any binary data returned by requests into image
#from PIL import Image
#from io import BytesIO

#i = Image.open(BytesIO(r.content))
