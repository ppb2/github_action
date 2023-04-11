import requests
import random
import time
import os

# curl 'https://glados.rocks/api/user/checkin' \
#   -H 'authority: glados.rocks' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'authorization: 85957412030771491941354582567954-982-1512' \
#   -H 'content-type: application/json;charset=UTF-8' \
#   -H 'cookie: _gid=GA1.2.271850584.1681198796; koa:sess=eyJ1c2VySWQiOjMyMzc4NCwiX2V4cGlyZSI6MTcwNzExODk4NzMwOSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=aPxv8aB8CL6ymvH8dYNkr3lN9Qw; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc; __stripe_mid=1d83459e-fc71-417a-810a-d462f6ae6a9a9a0ad2; __stripe_sid=e07c9303-157f-4cc4-a683-7c09e49e58fbdd1c01; _ga_CZFVKMNT9J=GS1.1.1681206844.4.1.1681206969.0.0.0; _ga=GA1.1.1628570063.1681198780' \
#   -H 'origin: https://glados.rocks' \
#   -H 'sec-ch-ua: "Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36' \
#   --data-raw '{"token":"glados.network"}' \
#   --compressed

url = "https://glados.rocks/api/user/checkin"

payload = "{\"token\":\"glados.network\"}"
headers = {
  'authority': 'glados.rocks',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'authorization': '85957412030771491941354582567954-982-1512',
  'content-type': 'application/json;charset=UTF-8',
  'cookie': '_gid=GA1.2.271850584.1681198796; koa:sess=eyJ1c2VySWQiOjMyMzc4NCwiX2V4cGlyZSI6MTcwNzExODk4NzMwOSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=aPxv8aB8CL6ymvH8dYNkr3lN9Qw; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc; __stripe_mid=1d83459e-fc71-417a-810a-d462f6ae6a9a9a0ad2; __stripe_sid=e07c9303-157f-4cc4-a683-7c09e49e58fbdd1c01; _ga_CZFVKMNT9J=GS1.1.1681206844.4.1.1681206969.0.0.0; _ga=GA1.1.1628570063.1681198780',
  'dnt': '1',
  'origin': 'https://glados.rocks',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

timeSecond = random.randint(1,59)
timeMin = random.randint(0,1)
# timeMin = 0
# time.sleep(timeSecond+timeMin*60)

response = requests.request("POST", url, headers=headers, data=payload)


if (response.text.find("Checkin! Get 1 Day") != -1):
  print("success")
elif (response.text.find("Please Try Tomorrow") != -1):
  print("success")
else:
  print("fail")



  




