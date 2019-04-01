import requests
import requests, re, json, datetime, os, hashlib, time, math


url = "http://web.canlitvlive.io/izle/trt-turk.html"
r = requests.post(url)
print(r.content)
data = r.content

re.findall('<ul>\s*(.*?)\s*<\/ul>', data, re.M|re.I|re.S)