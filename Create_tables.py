import json
from neo4j import GraphDatabase

conn = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

def serialize(dictio, remove=""):
    string = "{"
    for key, value in dictio.items():
        if key != remove:
            string += f'{key}:"{value}",'
    string = string[0:-1] + "}"

    return string

def createNode(liste, remove=""):
    for objet in liste:
        string = serialize(objet, remove=remove)
        with conn.session() as session:
            session.write_transaction(requestCreateNode, table, string)


def requestCreateNode(tx, table, string):
    requ = f"CREATE (:{table}{string})"
    tx.run(requ)
    print(requ)


with open("datas.json", "r") as read_file:
    jsonTables = json.load(read_file)

for table, datas in jsonTables.items():
    if table == "auth_user" or table == "shop_category" or table == "coupons_coupon":
        createNode(datas)

    if table == "orders_order":
        createNode(datas, remove="coupon_id")

    if table == "shop_product":
        createNode(datas, remove="category_id")

conn.close()
