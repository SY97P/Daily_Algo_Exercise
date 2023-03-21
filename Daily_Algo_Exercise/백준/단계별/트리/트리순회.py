# ABDCEFG
# DBAECFG
# DBEGFCA

import os

filename = "트리순회.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

def solve(node) :
    if node < 0 :
        return False

    prev.append(toStr(node))

    if not solve(adj[node][0]) :
        inor.append(toStr(node))
    if not solve(adj[node][1]) :
        post.append(toStr(node))

def toChar(s) :
    return s-ord('A')

def toStr(k) :
    return chr(k+ord('A'))

n = int(input())
adj = [tuple() for _ in range(26)]
for _ in range(n) :
    t, l, r = map(ord, input().split())
    adj[toChar(t)] = (toChar(l), toChar(r))

# for ad in adj :
#     print(ad)

prev = []
inor = []
post = []

solve(0)

print(''.join(prev))
print(''.join(inor))
print(''.join(post))


file.close()