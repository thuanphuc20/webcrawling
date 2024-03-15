from fastapi import FastAPI
import requests
import json
from bs4 import BeautifulSoup
app = FastAPI()

import json
@app.get("/api_craw")
def get_data():
    url = 'https://www.chotot.com/mua-ban-ha-noi'
    response = requests.get(url).content
 
    soup = BeautifulSoup(response, 'html.parser')
    data = []
    
    for item in soup.find_all('a',{"class":"AdItem_adItem__gDDQT"}):
        item_image = item.find('img')
        title_element = item.find('h3',{"class":"commonStyle_adTitle__g520j"})
        if title_element is not None:
            title = title_element.text
        else:
            title = "Unknown"
        detail_element = item.find('span',{"class":"AdBody_adItemCondition__ppptn"})
        if detail_element is not None:
            detail = detail_element.text
        else:
            detail = "Unknown"
        price_element = item.find('p',{"class":"AdBody_adPriceNormal___OYFU"})
        if price_element is not None:
            price = price_element.text
        else:
            price = "Unknown"
        image = item_image.get("src")
        href = item.get("href")
    
        data.append({'name': title, 'price': price, 'detai': detail, 'images': image ,'link': href})
        with open('../api_sql/data.json','w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
    
    
    return  data
#uvicorn api_craw:app --host 0.0.0.0 --port 8000