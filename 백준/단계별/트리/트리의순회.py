# 2 1 3
# 1 2 4 8 9 5 10 11 3 6 12 7

import os
filename = "트리의순회.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

def solve(inor_start, inor_end, post_start, post_end) :
    if inor_start > inor_end or post_start > post_end :
        return

    root = post[post_end]
    index = posi[root]

    print(root, end = " ")

    left = index - inor_start
    right = inor_end - index

    solve(inor_start, inor_start+left-1, post_start, post_start+left-1)
    solve(inor_end-right+1, inor_end, post_end-right, post_end-1)


n = int(input())
inor = list(map(int, input().split()))
post = list(map(int, input().split()))

posi = [0 for _ in range(n+1)]
for i in range(n) :
    posi[inor[i]] = i

solve(0, n-1, 0, n-1)

file.close()