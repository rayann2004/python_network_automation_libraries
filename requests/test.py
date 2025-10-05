import requests

print("Website Availability & Cookie-presence Checker")
print("Enter website names (type 'exit' when done):")

websites = []
while True:
    site = input("Website: ").strip()
    if site.lower() == "exit":
        break
    if not site:
        continue
    if "." not in site:
        site += ".com"
    if not site.startswith("http"):
        site = "https://" + site
    websites.append(site)

print("\nStarting check...\n")

for site in websites:
    try:
        # follow redirects by default (allow_redirects=True)
        r = requests.get(site, timeout=8)
        status = r.status_code
        cookie_present = bool(r.cookies)  # True if any cookies were set in response headers

        if status == 200:
            up_status = "[UP]   "
        else:
            up_status = "[WARN] "

        cookie_status = "[COOKIES]" if cookie_present else "[NO-COOKIES]"
        print(f"{up_status} {site} -> {status} {cookie_status}")

    except requests.exceptions.RequestException as e:
        print(f"[DOWN] {site} -> {e.__class__.__name__}")
