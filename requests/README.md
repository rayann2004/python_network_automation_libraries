is README includes excerpts and information from the official Requests documentation (https://pypi.org/project/requests/)

Requests is a Python library that makes sending HTTP requests simple and elegant. 
It handles all the low-level details like connections, headers, encoding, and JSON for you.

>>> import requests
>>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}


| Task                        | Without Requests       | With Requests             |
| --------------------------- | ---------------------- | ------------------------- |
| Connect to server           | Manual (`http.client`) | Automatic                 |
| Encode JSON                 | `json.dumps()`         | Automatic (`json=` param) |
| Set headers                 | Manual dictionary      | Automatic                 |
| Send request & read resp    | Multiple steps         | Single function call      |
| Total lines for simple POST | ~10+ lines             | 3–4 lines                 |

Installing Requests and Supported Versions
$ python -m pip install requests
   
