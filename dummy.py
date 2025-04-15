import math
def bell(arr,source):
    v=len(arr)
    dis=[math.inf for _ in range(v)]
    dis[source]=0

    for _ in range(v-1):
        update=False
        for i in range(v):
            for j in range(v):
                weight=arr[i][j]
                if dis[i]!=math.inf and arr[i][j]!=math.inf and weight+dis[i]<dis[j]:
                    dis[j]=weight+dis[i]
                    update=True
        if not update:
            break
    cycle=False
    for i in range(v):
            for j in range(v):
                weight=arr[i][j]
                if dis[i]!=math.inf and arr[i][j]!=math.inf and weight+dis[i]>dis[j]:
                    dis[j]=weight+dis[i]
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
