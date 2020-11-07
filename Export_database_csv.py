import sqlite3

tables = ["orders_order", "coupons_coupon", "orders_orderitem", "shop_product", "shop_category", "auth_user"]

with open('test.csv', 'w+') as write_file:
    conn = sqlite3.connect('db.sqlite3') # connect to your database 
    cursor = conn.cursor() # create a cursor object (which lets you address the table results individually) 
    for table in tables:
        write_file.write(table)
        for row in cursor.execute(f'SELECT * FROM {table}'): # use the cursor as an iterable 
            datas = ""
            for i in row:
                datas += f'{i},'

            write_file.write(";")
            write_file.write(datas) # write to the csv, then you can open the csv in Excel. 
        write_file.write("\n")

