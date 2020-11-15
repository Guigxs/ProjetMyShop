import json
from neo4j import GraphDatabase

conn = GraphDatabase.driver("bolt://54.160.119.107:35012", auth=("neo4j", "interpreters-flashes-soap"))

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
    if table == "auth_user" or table == "Category" or table == "Coupon":
        createNode(datas)

    if table == "Order":
        createNode(datas, remove="coupon_id")

    if table == "Product":
        createNode(datas, remove="category_id")

conn.close()
