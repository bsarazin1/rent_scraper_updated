import requests

r = requests.get('https://vermont.craigslist.org/search/apa?search_distance=10&postal=05404&min_price=&max_price=&availabilityMode=&sale_date=all+dates',
                 headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
print(r)
print(r.text)
a = (r.json())
print(a)
