# coding=utf-8
import requests

url = "http://schedule.unaux.com/"

payload = {
			"ilk_date":"2018-08-29",
			"son_date":"2018-09-09",
			"kanal":"TRTMÜZİK"
			}

headers = {
    'Cookie': "__test=fc4a3c7fe877f85c66434ff81453b13e",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)