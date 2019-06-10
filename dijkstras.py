nodes = ('A', 'B', 'C', 'D')
distances = {
    'B': {'A': 1, 'D': 2},
    'A': {'B': 1, 'D': 9, 'C' :1},
    'D': {'B': 2, 'C': 1, 'A': 9},
    'C': {'A': 1, 'D': 1}}

unvisited = {node: None for node in nodes} #using None as +inf

print (unvisited)
visited = {}
current = 'A'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        print(neighbour)
        print(unvisited)
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)