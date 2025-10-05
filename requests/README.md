# Requests Library

Requests is a Python library that makes sending HTTP requests simple and elegant. 
It handles all the low-level details like connections, headers, encoding, and JSON for you.

# Installing Requests and Supported Versions
$ python -m pip install requests
   

# Send a GET request

import requests

response = requests.get("https://httpbin.org/get")

print("Status Code:", response.status_code)

print("Content-Type:", response.headers['content-type'])

print("Response JSON:", response.json())


# Comparison of HTTP Requests in Python: Without vs With Requests

| Task                        | Without Requests       | With Requests             |
| --------------------------- | ---------------------- | ------------------------- |
| Connect to server           | Manual (`http.client`) | Automatic                 |
| Encode JSON                 | `json.dumps()`         | Automatic (`json=` param) |
| Set headers                 | Manual dictionary      | Automatic                 |
| Send request & read resp    | Multiple steps         | Single function call      |
| Total lines for simple POST | ~10+ lines             | 3–4 lines                 |

# Supported Features & Best–Practices

Keep-Alive & Connection Pooling.

International Domains and URLs.

Sessions with Cookie Persistence.

Browser-style TLS/SSL Verification.

Basic & Digest Authentication.

Familiar dict–like Cookies.

Automatic Content Decompression and Decoding.

Multi-part File Uploads.

SOCKS Proxy Support.

Connection Timeouts.

Streaming Downloads.

Automatic honoring of .netrc.

Chunked HTTP Requests.

is README includes excerpts and information from the official Requests documentation (https://pypi.org/project/requests/)

