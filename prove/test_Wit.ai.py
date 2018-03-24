import urllib3
https = urllib3.PoolManager()
req = https.request(method='GET', url='https://api.wit.ai/message?v=20170307&q=I%20hope%20my%20sister%20will%20win%20the%20competition')
req.add_header('Authorization', 'Bearer G6VIJLCU63GY3C3OYXNNSL6HUOBJ77YQ')
resp = https.urlopen(req)
content = resp.read()
print(content)
