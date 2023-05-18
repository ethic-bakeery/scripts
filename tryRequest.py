import urllib.request

with urllib.request.urlopen("https://www.htbsrmist.tech/team") as response:
   html = response.code
print(html)



import urllib.request

query_params = {'q': 'Python', 'page': 1, 'results_per_page': 10}
query_string = urllib.parse.urlencode(query_params)
url = f'https://www.htbsrmist.tech/{query_string}'
with urllib.request.urlopen(url) as response:
   search_results = response.read()
print(search_results)

