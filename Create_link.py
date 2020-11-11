import json
from neo4j import GraphDatabase

conn = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

def createLink(name, fromNode, toNode, linker, liste, id="id"):
    for objet in liste:
        if objet[linker]: 
            with conn.session() as session:
                session.write_transaction(requestCreateLink, name, fromNode, toNode, linker, objet, id)

def requestCreateLink(tx, name, fromNode, toNode, linker, objet, id):
    requ = f"MATCH (a:{fromNode}{{id:'{objet[id]}'}}), (b:{toNode}{{id:'{objet[linker]}'}}) CREATE (a)-[r:{name}]->(b)"
    tx.run(requ)
    print(requ)

with open("datas.json", "r") as read_file:
    jsonTables = json.load(read_file)

for table, datas in jsonTables.items():
    if table == "orders_order":
        createLink("USE", "orders_order", "coupons_coupon", "coupon_id", datas)

    if table == "shop_product":
        createLink("PART_OF", "shop_product", "shop_category", "category_id", datas)

    if table == "orders_orderitem":
        createLink("CONTAINS", "orders_order", "shop_product", "product_id", datas, id="order_id")