import sqlite3
import json

tables = ["orders_order", "coupons_coupon", "orders_orderitem", "shop_product", "shop_category", "auth_user"]
tablesNew = ["Order", "Coupon", "orders_orderitem", "Product", "Category", "auth_user"]

conn = sqlite3.connect('db.sqlite3') # connect to your database 
cursor = conn.cursor() # create a cursor object (which lets you address the table results individually) 
jsonTables = {}
for i in range(len(tables)):
    liste = []
    for row in cursor.execute(f'SELECT * FROM {tables[i]}'): # use the cursor as an iterable 
        liste.append(list(row))
    fields = [a[0] for a in cursor.description]

    objetListe = []
    for j in range(len(liste)):
        objet = {}
        for k in range(len(fields)):
            objet[fields[k]] = liste[j][k]
        
        objetListe.append(objet)
        
    jsonTables[tablesNew[i]] = objetListe

with open('datas.json', 'w') as write_file:
    json.dump(jsonTables, write_file)


