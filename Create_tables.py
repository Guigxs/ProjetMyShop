# from py2neo import Graph

# graph = Graph()
# tx = graph.begin()

with open("test.csv", "r") as read_file:
    lines = read_file.readlines()
    for line in lines:
        table = line.split(";")
        table_name = table[0]
        table_data = table[1:-1]

    
        # for data in range(len(table)):

