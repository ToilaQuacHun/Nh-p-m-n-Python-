from collections import deque
from itertools import combinations
adj = [
    [0,1,1,0,1],
    [1,0,1,1,0],
    [1,1,0,1,0],
    [0,1,1,0,1],
    [1,0,0,1,0]
]





#tinh bac cua dinh
def degree_list(adj):
    n=len(adj)
    deg=[0]*n
    for i in range(n):
        deg[i]=sum(adj[i])
    return deg

#xet tinh lien thong
def is_connected(adj):
    n=len(adj)
    visited = [False] * n
    q = deque([0])
    visited[0] = True 
    while q:
        u = q.popleft()
        for v in range (n):
            if adj[u][v] == 1 and not visited[v]:
                visited[v]=True
                q.append(v)
    return all (visited)

#Dirac theorem
def check_dirac(adj):
    n = len (adj)
    deg = degree_list(adj)
    for d in deg:
        if d<n/2:
            return False
    return True

#Ore theorem 
def check_ore(adj):
    n=len(adj)
    deg = degree_list(adj)
    for i in range(n):
        for j in range(i+1,n):
            if adj[i][j]==0:
                if deg[i]+deg[j]<n:
                    return False
    return True 

#kiem tra ban hamilton 
def check_semi_hamilton_condition(adj):
    n = len(adj)
    deg=degree_list(adj)
    for d in deg:
        if d<(n-1)/2:
            return False
    return True 

#theorem 2
#dem so thanh phan lien thong sau khi bo mot so dinh
def count_components_after_removal(adj,removed):
    n=len(adj)
    removed = set(removed)
    visited = [False] * n
    components = 0 
    for start in range (n):
        if start in removed or visited[start]:
            continue
        components +=1
        q=deque([start])
        visited[start]=True
        while q:
            u = q.popleft()
            for v in range(n):
                if v not in removed and not visited[v] and adj[u][v] == 1:
                    visited[v] = True 
                    q.append(v)
    return components

#kiem tra theorem 2 
def violates_theorem_2(adj,max_k=2):
    n=len(adj)
    for k in range(1, min(max_k,n)+1):
        for removed in combinations(range(n),k):
            components = count_components_after_removal(adj,removed)
    return False, None, None

def identify_graph(adj):
    if not is_connected(adj):
        return " Khong Lien Thong"
    if check_dirac(adj):
        return "Hamilton theo dly Dirac"
    if check_ore(adj):
        return "Hamilton theo dly Ore"
    if check_semi_hamilton_condition(adj):
        return "Do thi semi-Hamilton"
    bad, removed, comp = violates_theorem_2(adj, max_k=2)
    if bad: 
        return f" Do thi khong hamilton (bo{len(removed)} dinh {removed} thi có {comp} thành phần liên thông > {len(removed)})"
    return "khong ket luan duoc"

print (adj)
print (identify_graph(adj))





