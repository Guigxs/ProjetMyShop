import json
from neo4j import GraphDatabase

conn = GraphDatabase.driver("bolt://54.160.119.107:35012", auth=("neo4j", "interpreters-flashes-soap"))

def createLink(name, fromNode, toNode, linker, liste, id="id", quantity=None):
    for objet in liste:
        if quantity:
            quantity = objet["quantity"]
        if objet[linker]: 
            with conn.session() as session:
                session.write_transaction(requestCreateLink, name, fromNode, toNode, linker, objet, id, quantity)

def requestCreateLink(tx, name, fromNode, toNode, linker, objet, id, quantity):
    if quantity:
        requ = f"MATCH (a:{fromNode}{{id:'{objet[id]}'}}), (b:{toNode}{{id:'{objet[linker]}'}}) CREATE (a)-[r:{name}{{quantity:{quantity}}}]->(b)"
    else:
        requ = f"MATCH (a:{fromNode}{{id:'{objet[id]}'}}), (b:{toNode}{{id:'{objet[linker]}'}}) CREATE (a)-[r:{name}]->(b)"
    tx.run(requ)
    print(requ)

with open("datas.json", "r") as read_file:
    jsonTables = json.load(read_file)

for table, datas in jsonTables.items():
    if table == "Order":
        createLink("USE", "Order", "Coupon", "coupon_id", datas)

    if table == "Product":
        createLink("PART_OF", "Product", "Category", "category_id", datas)

    if table == "orders_orderitem":
        createLink("CONTAINS", "Order", "Product", "product_id", datas, id="order_id", quantity=1)