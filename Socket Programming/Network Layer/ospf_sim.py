# ospf_sim.py
# Simplified OSPF (link-state) simulation using Dijkstra
import networkx as nx

def build_topology():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ('A','B',2),('A','C',5),('B','C',1),('B','D',2),('C','E',3),('D','E',1)
    ])
    return G

def compute_lsa_and_routes(G):
    routes = {}
    for node in G.nodes():
        lengths, paths = nx.single_source_dijkstra(G, node)
        routes[node] = {dest: (lengths.get(dest,float('inf')), paths.get(dest,[])) for dest in G.nodes()}
    return routes

def run():
    G = build_topology()
    routes = compute_lsa_and_routes(G)
    print("OSPF: Shortest paths (cost, path) per router:")
    for r, tbl in sorted(routes.items()):
        print("Router", r)
        for dest in sorted(tbl.keys()):
            cost, path = tbl[dest]
            print("  ->", dest, ": cost=", cost, ", path=", path)
        print("")

if __name__ == '__main__':
    run()
