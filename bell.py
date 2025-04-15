import math
def bell(mat,source):
    v=len(mat)
    dis=[math.inf]*v
    dis[source]=0

    for _ in range (v-1):
        update=False
        for i in range(v):
            for j in range(v):
                weight=mat[i][j]
                if weight!=math.inf and dis[i]!=math.inf and dis[j]>dis[i]+weight:
                    dis[j]=dis[i]+weight
                    update=True
                
            if not update:
                break
    cycle=False
    for i in range(v):
        for j in range(v):
            weight=mat[i][j]
            if weight!=math.inf and dis[i]!=math.inf and dis[j]>dis[i]+weight:
                dis[j]=dis[i]+weight
                cycle=True
        if cycle:
            break

    return dis,cycle

graph = [
    [0, 1, 4, math.inf, math.inf],
    [math.inf, 0, 2, 5, math.inf],
    [math.inf, math.inf, 0, 1, 3],
    [math.inf, math.inf, math.inf, 0, 1],
    [math.inf, math.inf, math.inf, math.inf, 0]
]
source = 0

distances, negative_cycle = bell(graph, source)
print("Shortest distances:", distances)
print("Negative cycle detected:", negative_cycle)