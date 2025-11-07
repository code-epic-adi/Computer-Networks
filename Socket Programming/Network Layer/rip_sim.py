# rip_sim.py
# Simplified RIP (distance-vector) simulation
import networkx as nx

def build_topology():
    G = nx.Graph()
    edges = [('R1','R2'),('R1','R3'),('R2','R3'),('R2','R4'),('R3','R5'),('R4','R5')]
    G.add_edges_from(edges)
    return G

def init_tables(G):
    tables = {}
    for n in G.nodes():
        tables[n] = {dest: (0 if dest==n else float('inf')) for dest in G.nodes()}
        for nei in G.neighbors(n):
            tables[n][nei] = 1
    return tables

def exchange_once(G, tables):
    updated = False
    for router in list(G.nodes()):
        for neighbor in G.neighbors(router):
            neigh_table = tables[neighbor]
            for dest, dcost in neigh_table.items():
                new_cost = 1 + dcost
                if new_cost < tables[router].get(dest, float('inf')):
                    tables[router][dest] = new_cost
                    updated = True
    return updated

def run(max_iters=50):
    G = build_topology()
    tables = init_tables(G)
    it = 0
    while it < max_iters:
        it += 1
        changed = exchange_once(G, tables)
        if not changed:
            break
    print("RIP converged in", it, "iterations")
    for r, tbl in sorted(tables.items()):
        formatted = {k: (v if v!=float('inf') else 'inf') for k,v in tbl.items()}
        print("Router", r, "table:", formatted)

if __name__ == '__main__':
    run()
