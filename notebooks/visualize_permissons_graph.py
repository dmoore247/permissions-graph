# Databricks notebook source
# MAGIC %pip install --quiet pyvis rdflib kglab

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from pyvis.network import Network
import pandas as pd

got_net = Network(height='750px', width='80%', bgcolor='#222222', font_color='white', directed=True)

# set the physics layout of the network
got_net.barnes_hut()
got_data = CHF_model_transition_graph

sources = got_data['Source']
targets = got_data['Target']
weights = got_data['Weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
got_net.write_html('CHF.html')
CHF_html= open("CHF.html", "r").read()
displayHTML(CHF_html)

# COMMAND ----------

import pyvis.network

pyvis_graph = pyvis.network.Network(notebook=True,cdn_resources = 'remote')

pyvis_graph.add_node(0, label="foo", title="This is FOO", color="orange", size=9)
pyvis_graph.add_node(1, label="bar", title="That is BAR", color="blue", size=5)
pyvis_graph.add_node(2, label="baz", title="Here is BAZ", color="green", size=3)

pyvis_graph.add_edge(0, 1, label="xyzzy", color="gray")
pyvis_graph.add_edge(0, 2, label="fubar", color="red")

pyvis_graph.force_atlas_2based()
pyvis_graph.show(name="bob.html", )

html = open("bob.html",'r').read()
displayHTML(html)

# COMMAND ----------

import pyvis.network

pyvis_graph = pyvis.network.Network(notebook=True,cdn_resources = 'remote', )

pyvis_graph.add_node(0, label="foo", title="This is FOO", color="orange", size=9)
pyvis_graph.add_node(1, label="bar", title="That is BAR", color="blue", size=5)
pyvis_graph.add_node(2, label="baz", title="Here is BAZ", color="green", size=3)

pyvis_graph.add_edge(0, 1, label="xyzzy", color="gray")
pyvis_graph.add_edge(0, 2, label="fubar", color="red")

pyvis_graph.force_atlas_2based()

pyvis_graph.show_buttons(filter_=['physics'])

# COMMAND ----------


