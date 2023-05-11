import psycopg2
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
matplotlib.use('TkAgg')

conn = psycopg2.connect(
    host="encrypted-tao.clyigb9dssrd.us-east-1.rds.amazonaws.com",
    database="postgres",
    user="dbuser",
    password="dbuserdbuser"
)

with conn.cursor() as cur:
    cur.execute('SELECT id, otype FROM Objrow')
    objects_query = cur.fetchall()
    cur.execute('SELECT id1, id2, atype FROM Assocrow')
    associations_query = cur.fetchall()

G = nx.DiGraph()

for obj in objects_query:
    G.add_node(obj[0], otype=obj[1])

for assoc in associations_query:
    G.add_edge(assoc[0], assoc[1], atype=assoc[2])

fig, ax = plt.subplots()

pos = nx.spring_layout(G)
node_labels = nx.get_node_attributes(G, 'otype')
edge_labels = nx.get_edge_attributes(G, 'atype')

user_nodes = [n for n, attr in G.nodes(data=True) if attr["otype"] == "USER"]
post_nodes = [n for n, attr in G.nodes(data=True) if attr["otype"] == "POST"]

nx.draw_networkx_nodes(G, pos, nodelist=user_nodes, node_color="blue", node_size=200)
nx.draw_networkx_nodes(G, pos, nodelist=post_nodes, node_color="red", node_size=200)

nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=5)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=5)

canvas = FigureCanvasTkAgg(fig, master=tk.Tk())
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar = NavigationToolbar2Tk(canvas, tk.Tk())
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

tk.mainloop()