# My Shop NoSQL Project 2020-2021
Authors : Guillaume Ceastecker - Guillaume Bouillon

## Steps
### Booste DB performances

1. [V] Implement a recomandation system on the product page
2. [V] Implement a view counter on the product page
3. [V] Use Redis (NoSQL DB) as a django cache

### Design a new NoSQL DB

1. [V] Choose a Neo4j or MongoDB model
2. [V] Create a new database with the chosen model
3. [V] Migrate automatically the all data to the new database

### Integrate new database in django

1. [] Have a working site with the new database
2. [] Host the database on a remote server


## How to migrate to new NoSQL databse
First, create a [remote](https://sandbox.neo4j.com/) or a local databse with Neo4j

Install the new requirements:
```console
pip install -r requirements.txt
```
>Note: using a virtual environement is a good practice.

Then, update the connection settings in the `Create_tables.py` and `Create_link.py` files with your database ardress.

Finally, run:
```console
Migrate_database_to_noe4j.py
```

Done.