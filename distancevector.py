import networkx as nx

def add_link(graph, node1, node2, cost):
    graph.add_edge(node1, node2, weight=cost)

def print_routing_table(graph, nodes, source):
    print(f"Routing table for Node {source}:")
    print("Destination\tCost")
    distances = nx.single_source_dijkstra_path_length(graph, source, weight='weight')
    for dest in nodes:
        cost = distances.get(dest, float('inf'))
        print(f"{dest}\t\t{cost}")

# Example usage
nodes = [1, 2, 3, 4, 5]
graph = nx.Graph()

add_link(graph, 1, 2, 2)
add_link(graph, 1, 3, 2)
add_link(graph, 1, 4, 1)
add_link(graph, 2, 3, 3)
add_link(graph, 2, 1, 2)
add_link(graph, 2, 5, 1)
add_link(graph, 3, 1, 2)
add_link(graph, 3, 4, 4)
add_link(graph, 3, 2, 3)
add_link(graph, 3, 5, 1)
add_link(graph, 4, 1, 1)
add_link(graph, 4, 3, 4)
add_link(graph, 5, 2, 1)
add_link(graph, 5, 3, 1)

for node in nodes:
    print_routing_table(graph, nodes, node)
