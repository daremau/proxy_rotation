import requests

with open('valid_proxy.txt', 'r') as file:
    proxies = file.read().split('\n')
  
sites_to_check = ['http://books.toscrape.com/', 
                  'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
                  'http://books.toscrape.com/catalogue/category/books/history_32/index.html']

counter = 0

for site in sites_to_check:
    try:
        print(f"using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http": proxies[counter], "https": proxies[counter]})
        print(res.status_code)

    except:
        print('Failed')
    finally:
        counter += 1
        # if having more sites to check than valid proxies
        #counter % len(proxies)