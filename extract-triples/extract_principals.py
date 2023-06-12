from principals import *
from utils import save_graph
from config import *


walkers = [
    { "name": "groups", "func": walk_groups},
    { "name": "users",  "func": walk_users}
]

def graph_name(hostname, client_name, walker_name):
    return f'graph_{client_name}_{walker_name}'

def extract_principals(spark, clients):
    counter = 0
    for client in clients:
        for walker in walkers:
            client_name = client['name']
            client_obj = client['client']
            walker_name = walker['name']
            walker_func = walker['func']
            
            triples =  walker_func(client_obj)
            print(f'{client_name} {walker_name} triples count: {len(triples)}')
            # Save to KG
            name = graph_name("e2-demo", client_name, walker_name)
            save_graph(spark, triples, name)
            counter = counter + 1
    return counter
