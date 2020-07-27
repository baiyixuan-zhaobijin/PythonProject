from urllib import request
response = request.urlopen(r'https://jixi.58.com/ershouche/pn1/?PGTID=0d100000-01c7-92a6-616f-3afaed1bae9c&ClickID=57/') # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
page = response.read()
page = page.decode('utf-8')
print(page)