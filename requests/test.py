import requests

print(" Website Availability Checker")
print("Enter website names (type 'exit' when done):")

websites = []

while True:
    site = input("Website: ")
    if site.lower() == "exit":
        break
    

    if "." not in site:
        site = site + ".com"
    
    
    if not site.startswith("http"):
        site = "https://" + site
    
    websites.append(site)

print("\n Starting check...\n")

for site in websites:
    try:
        r = requests.get(site, timeout=5)
        if r.status_code == 200:
            print(f"[UP]   {site} -> {r.status_code}")
        else:
            print(f"[WARN] {site} -> {r.status_code}")
    except requests.exceptions.RequestException:
        print(f"[DOWN] {site}")
