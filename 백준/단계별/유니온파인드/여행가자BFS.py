# YES
# YES

import os
filename = "여행가자.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

from collections import deque

def bfs(num, q) :
    global visited

    while q :
        node = q.popleft()

        for next_node in adj[node] :
            if visited[next_node] == 0 :
                visited[next_node] = num
                q.append(next_node)


n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for i in range(1, n+1) :
    temp = list(map(int, input().split()))
    for j in range(n) :
        if temp[j] :
            adj[i].append(j+1)

paths = list(map(int , input().split()))

visited = [0 for _ in range(n+1)]
for node in range(1, n+1) :
    if visited[node] == 0 :
        visited[node] = node
        bfs(node, deque([node]))

grand_parent = visited[paths[0]]
connected = True

for path in paths :
    if grand_parent != visited[path] :
        connected = False
        break

print("YES" if connected else "NO")

file.close()