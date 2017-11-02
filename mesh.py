import requests
import time

headers1 = {
    'Host': 'commerce.mesh.mx',
    'Content-Type': 'application/json',
    'X-API-Key': '5F9D749B65CD44479C1BA2AA21991925',
    'Accept': '*/*',
    'X-Debug': '1',
    'Accept-Language': 'en-gb',
    'User-Agent': 'FootPatrol/2.0 CFNetwork/808.3 Darwin/16.3.0',
    'MESH-Commerce-Channel': 'iphone-app',
}

params = (
    ('expand', 'variations,informationBlocks,customisations'),
    ('channel', 'iphone-app'),
)


start_number = 300000
for i in range(start_number-1,0,-1):
    time.sleep(5)
    print(i)
    stock_json_raw = requests.get('https://commerce.mesh.mx/stores/footpatrol/products/' + str(i), headers=headers1, params=params).text.strip()
    print(stock_json_raw)


#print(stock_json_raw)
print(i)
print('='*10)



