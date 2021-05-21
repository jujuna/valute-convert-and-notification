import requests
import json

def req():
    url='https://bankofgeorgia.ge/api/currencies/getCurrenciesList/pages/5c0a361ff85d2d574073cf30'
    resp=requests.get(url=url)
    data=resp.json()

    with open('api.json', 'w', encoding='utf-8') as file:
        json.dump(data,file,indent=4,sort_keys=True,ensure_ascii=False)


    f=open('api.json', encoding='utf-8')
    data=json.load(f)

    return data



