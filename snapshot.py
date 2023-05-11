import psycopg2
import networkx as nx
import json

conn = psycopg2.connect(
    host="encrypted-tao.clyigb9dssrd.us-east-1.rds.amazonaws.com",
    database="postgres",
    user="dbuser",
    password="dbuserdbuser"
)

with conn.cursor() as cur:
    cur.execute('SELECT id, otype, data FROM Obj_decrypt')
    objects_query = cur.fetchall()
    cur.execute('SELECT id1, id2, atype FROM Assoc_decrypt')
    associations_query = cur.fetchall()

G = nx.DiGraph()

for obj in objects_query:
    G.add_node(obj[0], otype=obj[1], data=obj[2])

for assoc in associations_query:
    G.add_edge(assoc[0], assoc[1], atype=assoc[2])

graph_data = {"nodes": [], "links": []}


for node in G.nodes(data=True):
    graph_data["nodes"].append({"id": node[0], "otype": node[1]["otype"], "data": node[1]["data"]})

for edge in G.edges(data=True):
    graph_data["links"].append({"source": edge[0], "target": edge[1], "atype": edge[2]["atype"]})

json_data = json.dumps(graph_data)

with open("graph_data.json", "w") as outfile:
    outfile.write(json_data)
