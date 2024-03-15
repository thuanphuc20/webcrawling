from fastapi import FastAPI
import json

import mysql.connector
app = FastAPI()


cnx = mysql.connector.connect(user='root', password='pws123', port='3306',
                                host='localhost',
                                database='local_db')


def insert_data(name, price, detai, images, link):
    mycursor = cnx.cursor()
    sql = "INSERT INTO mondo1 (name, price, detail, image , link) VALUES (%s, %s, %s, %s, %s)"
    val = (name, price, detai, images, link)
    mycursor.execute(sql, val)
    cnx.commit()

@app.post("/insert_data")
async def get_data():
    with open('data.json', 'r' ,encoding='utf-8') as f:
        data = json.load(f)        
    for item in data:
        insert_data(item["name"], item["price"], item["detai"], item["images"], item["link"])    
    
    return {"message": "Dữ liệu đã được insert thành công"}

def search_data(keyword):
    mycursor = cnx.cursor()
    sql = "SELECT * FROM mondo1 WHERE name LIKE %s"
    val = ("%{}%".format(keyword), )
    mycursor.execute(sql, val)
    rows = mycursor.fetchall()

    
    data = []
    for row in rows:
        item = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "detail": row[3],
            "image":row[4],
            "link": row[5]
        }
        data.append(item)

    
    return (data)


@app.get("/search")
async def search(keyword: str):
    data = search_data(keyword)
    return {"data": data}