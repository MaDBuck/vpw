from collections import defaultdict
from heapq import heapify, heappop, heappush


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, from_node, to_node, cost, directed=False):
        if cost < 0: raise ValueError("Costs must be non-negative for dijkstra to work")

        self.adj_list[from_node].append((to_node, cost))
        if not directed:
            self.add_edge(to_node, from_node, cost, True)


def dijkstra(graph, source, destination):
    distance = {source: 0}
    queue = [(distance[source], source)]
    heapify(queue)

    while queue:
        (d, u) = heappop(queue)
        if u == destination: return d

        for v, w in graph.adj_list[u]:
            if (v not in distance) or ((d + w) < distance[v]):
                distance[v] = d + w
                heappush(queue, (distance[v], v))


import copy
import io
import itertools
import sys
from math import isinf

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)

k = int(input())
for t in range(k):
    maximum_d, crossroads, streets = list(map(int, input().split(" ")))
    graph = Graph()
    shortest_distances = [None] * crossroads
    for x in range(crossroads):
        shortest_distances[x] = [float('inf')] * crossroads
    for x in range(streets):
        i, j, s = list(map(int, input().split(" ")))
        graph.add_edge(j - 1, i - 1, s, directed=False)
    # Calculate distances between crossroads naively
    for x in range(crossroads):
        for y in range(x, crossroads):
            d = dijkstra(graph, x, y)
            if d is None:
                d = float('inf')
            shortest_distances[x][y] = d
            shortest_distances[y][x] = d


    def add_one(tup):
        return [x + 1 for x in tup]


    # Start with smallest size
    for i in range(1, crossroads + 1):
        solutions = []
        smallest = float('inf')
        for combination in itertools.combinations(range(crossroads), i):
            all_distances = [min(shortest_distances[i][x] for x in combination) for i in range(crossroads)]
            if all(distance <= maximum_d for distance in all_distances):
                total = sum(all_distances)
                if total == smallest:
                    solutions.append(" ".join(list(map(str, add_one(combination)))))
                elif total < smallest:
                    solutions = [" ".join(list(map(str, add_one(combination))))]
                    smallest = total
        if solutions:
            for solution in sorted(solutions):
                print(t + 1, solution)
            break
