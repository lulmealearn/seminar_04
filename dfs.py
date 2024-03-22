edge_list = [
    [0, 1], [0, 3],
    [1, 3], 
    [2, 3], 
    [4, 0], [4, 3],
    [5, 0]
]
vert_num = 6

adj_list = [[] for _ in range(vert_num)] 
for edge in edge_list:
    u = edge[0]
    v = edge[1]
    adj_list[u].append(v)

print(adj_list)

g = adj_list
parents = [None for i in range(vert_num)]
colors = ["w" for i in range(vert_num)]
timer = 0
tin = [None for i in range(vert_num)]
tout = [None for i in range(vert_num)]
paths = [0] * vert_num  

def dfs(v, p=-1):
    global timer
    parents[v] = p
    colors[v] = "g"
    timer += 1
    tin[v] = timer   
    
    for u in g[v]:
        if colors[u] == "g":
            print(f"found cycle {v}->{u}")
            continue
        elif colors[u] == "b":
            continue
        elif colors[u] == "w":
            dfs(u, v)

    colors[v] = "b"
    timer += 1
    tout[v] = timer

def top_sort():
    for v in range(vert_num):
        if colors[v] == "w":
            dfs(v)

    vert_list = [i for i in range(vert_num)]
    ans = [
        x for y, x in sorted(zip(tout, vert_list), key=lambda pair: pair[0], reverse = True)
    ]
    return ans
    
ts = top_sort()
path = [1] * len(ts)  
index_dict = {vertex: idx for idx, vertex in enumerate(ts)}

for vertex in reversed(ts[:-1]):  
    vertex_index = index_dict[vertex]
    adjacent_vertices = adj_list[vertex]
    
    for adj_vertex in adjacent_vertices:
        adj_vertex_index = index_dict[adj_vertex]
        path[vertex_index] += path[adj_vertex_index]

print(path)    
