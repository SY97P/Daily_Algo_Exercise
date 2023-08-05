# 3
# 5
# 4

import os

filename = "뱀과사다리게임.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

from collections import deque

def solve(q) :
    result = float('inf')

    visited = [False for _ in range(107)]
    visited[1] = True

    while q:
        count, curr = q.popleft()

        if curr > 100 :
            continue
        elif curr == 100 :
            result = min(result, count)

        for i in range(1, 7) :
            if not visited[curr+i] :
                if curr+i in gimmick.keys() :
                    visited[curr+i] = True
                    q.append((count+1, gimmick[curr+i]))
                else :
                    visited[curr+i] = True
                    q.append((count+1, curr+i))

    return result


# for tc in range(3) :
n, m = map(int, input().split())
gimmick = dict()
for _ in range(n+m) :
    a, b = map(int, input().split())
    gimmick[a] = b

print(solve(deque([(0, 1)])))

file.close()