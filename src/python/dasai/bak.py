import httplib
conn = httplib.HTTPConnection('www.baidu.com')
conn.request("GET", "")
r1 = conn.getresponse()
print r1.status, r1.reason
data = r1.read()
print  data

conn = httplib.HTTPConnection('opendata.sz.gov.cn')
conn.request("GET", "/api/798418111/1/service.xhtml?page=1&rows=100&appKey=d287c7d3e868497a8805ff62df802214")
r1 = conn.getresponse()
print r1.status, r1.reason
data = r1.read()
print  data