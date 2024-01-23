import networkx as nx

def add_link(graph, start, end, cost):
    graph.add_edge(start, end, weight=cost)

nodes = [1, 2, 3, 4]
graph = nx.Graph()

add_link(graph, 1, 2, 2)
add_link(graph, 1, 3, 2)
add_link(graph, 1, 4, 1)
add_link(graph, 2, 3, 3)
add_link(graph, 2, 1, 2)
add_link(graph, 3, 1, 2)
add_link(graph, 3, 4, 4)
add_link(graph, 4, 1, 1)


for source in nodes:
    print(f"Routing table for Node {source}:")
    print("Destination\tCost")
    distances = nx.single_source_dijkstra_path_length(graph, source, weight='weight')
    for dest in nodes:
        cost = distances.get(dest, float('inf'))
        print(f"{dest}\t\t{cost}")
    print()
