# isis_sim.py
# Simplified IS-IS (link-state) simulation using Dijkstra
import networkx as nx

def build_topology():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ('X','Y',1),('X','Z',4),('Y','Z',2),('Y','W',3),('Z','W',1)
    ])
    return G

def compute_shortest_paths(G):
    db = G.copy()  # assume flooding synchronizes the LSDB
    routes = {}
    for n in db.nodes():
        lengths, paths = nx.single_source_dijkstra(db, n)
        routes[n] = {dest: (lengths.get(dest,float('inf')), paths.get(dest,[])) for dest in db.nodes()}
    return routes

def run():
    routes = compute_shortest_paths(build_topology())
    print("IS-IS routing tables (cost, path):")
    for r,tbl in sorted(routes.items()):
        print("Router", r)
        for dest in sorted(tbl.keys()):
            cost, path = tbl[dest]
            print("  ->", dest, ": cost=", cost, ", path=", path)
        print("")

if __name__ == '__main__':
    run()
