import urllib2
req = urllib2.Request('https://api.wit.ai/message?v=20170307&q=Monsters%20is%20stronger%20than%20Nilfgaard')
req.add_header('Authorization', 'Bearer HVRIVMJNL3SEGWJYFXM7S7KYNUNMYD35')
resp = urllib2.urlopen(req)
content = resp.read()
print content