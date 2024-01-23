import networkx as nx

def add_link(graph, start, end, cost):
    graph.add_edge(start, end, weight=cost)

nodes = [1, 2, 3, 4, 5]
graph = nx.Graph()

add_link(graph, 1, 2, 2)
add_link(graph, 1, 3, 2)
add_link(graph, 1, 4, 1)
add_link(graph, 2, 3, 3)
add_link(graph, 2, 1, 2)
add_link(graph, 3, 1, 2)
add_link(graph, 3, 2, 3)
add_link(graph, 3, 4, 4)
add_link(graph, 4, 1, 1)
add_link(graph, 4, 3, 4)
add_link(graph, 5, 3, 1)  # node 5 which is only conneted to node 3 

for node in nodes:
    print(f"Routing table for Node {node}:")
    print("dest\tCost")
    distances = nx.single_source_dijkstra_path_length(graph, node, weight='weight')
    for destination in nodes:
        cost = distances.get(destination, float('inf'))
        print(f"{destination}\t{cost}")
    print()
