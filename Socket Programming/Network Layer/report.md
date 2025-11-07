Routing Protocols Simulation

Topologies used:
- RIP: 6 nodes (R1..R5) with a small mesh to demonstrate alternate paths and convergence.
- OSPF: 5 nodes (A..E) with weighted links to model link costs.
- BGP: 5 ASes (AS1..AS5), AS5 originates prefix P.
- IS-IS: 4 nodes (X..W) with weighted links.

Part 1 — RIP (Distance-Vector)
- Implementation: routers maintain distance vectors (hop counts). Periodic neighbor exchanges update tables until no change.
- Observation: Converges in a small number of iterations for this topology. In larger/more pathological topologies, RIP is subject to slow convergence and count-to-infinity issues; split horizon / poison reverse reduce some issues (not implemented here).

Part 2 — OSPF (Link-State)
- Implementation: LSDB assumed synchronized; each router runs Dijkstra to compute shortest-path tree using link costs.
- Observation: Link-state scales better and converges faster for link changes because each router has complete topology (LSA flooding cost vs periodic full-table exchanges).

Part 3 — BGP (Path-Vector)
- Implementation: AS-level route propagation. Routes carry AS_PATH lists; neighbors choose route with shortest AS_PATH length. Loop prevention: route is discarded if local AS is already in AS_PATH.
- Observation: BGP is policy-rich in real networks; this sim demonstrates AS_PATH-based loop prevention and incremental propagation.

Part 4 — IS-IS (Link-State)
- Implementation and behavior similar to OSPF in this lab: LSDB flooding (assumed reliable) and Dijkstra per router.
- Observation: IS-IS and OSPF provide similar functionality; differences in protocol encoding and deployment exist in the real world.

Comparison and conclusions:
- RIP is simple but not suitable for large or rapidly changing networks.
- OSPF/IS-IS (link-state) provide better scalability and faster convergence at cost of LSDB flooding and more state.
- BGP (path-vector) is designed for inter-AS policy and scalability; AS_PATH provides loop prevention.
