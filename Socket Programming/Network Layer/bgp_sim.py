# bgp_sim.py
# Simplified BGP (path-vector) simulation (AS-level)
def build_as_topology():
    AS = {
        'AS1': ['AS2','AS3'],
        'AS2': ['AS1','AS4'],
        'AS3': ['AS1','AS4'],
        'AS4': ['AS2','AS3','AS5'],
        'AS5': ['AS4']
    }
    origins = {'P':'AS5'}  # AS5 originates prefix P
    return AS, origins

def run(max_iters=20):
    AS, origins = build_as_topology()
    routes = {asn: {} for asn in AS}
    for p, origin in origins.items():
        routes[origin][p] = [origin]

    it = 0
    changed = True
    while changed and it < max_iters:
        it += 1
        changed = False
        for asn in AS:
            for neigh in AS[asn]:
                for prefix, aspath in list(routes[asn].items()):
                    new_path = aspath.copy()
                    if neigh in new_path:
                        continue
                    candidate = new_path + [asn]
                    old = routes[neigh].get(prefix)
                    if old is None or len(candidate) < len(old):
                        routes[neigh][prefix] = candidate
                        changed = True
    print("BGP converged in", it, "iterations")
    for asn in sorted(routes.keys()):
        print(asn + ":")
        for p, path in routes[asn].items():
            print(" ", p, "-> AS_PATH:", path)

if __name__ == '__main__':
    run()
