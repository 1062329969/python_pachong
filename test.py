import re
import requests

url = "https://cdn.oursketch.com/FSHN%20Fashion%20E-Commerce%20App%20UI.sketch"

payload = {}
headers = {
  # ':authority': 'cdn.oursketch.com',
  # ':method': 'GET',
  # ':path': '/FSHN%20Fashion%20E-Commerce%20App%20UI.sketch',
  # ':scheme': 'https',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cache-control': 'no-cache',
  'cookie': 'Hm_lvt_70a1d60c3498fd09334af15ab61ef4d8=1576738250; Hm_lpvt_70a1d60c3498fd09334af15ab61ef4d8=1577065584',
  'pragma': 'no-cache',
  'referer': 'https://oursketch.com/resource',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data = payload)
f = open(r"E:\demo.sketch", "wb")
print('start')
for chunk in response.iter_content(chunk_size=500):
  if chunk:
    f.write(chunk)
print('end')



# print(response.text.encode('utf8'))


# imgre = re.findall(r'(.*)/(.*)', 'https://images.pexels.com/photos/416405/pexels-photo-416405.jpeg')
# print(imgre[0][1])
