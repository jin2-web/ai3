import requests as req

url = 'http://search.naver.com/search.naver'
res = req.get(url,params={'query':'파이썬'})

print(res.text)