# 5
# 28
# 24
# 45
# 30
# 60
# 52
# 98
# 50

import os
filename = "이진검색트리.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

# import sys
#
# input = sys.stdin.readline
#
# sys.setrecursionlimit(10**6)

def solve(start, end) :
    if start == end :
        # print("break")
        return

    curr = inor[start]

    left, right = count(curr, start, end)

    # print("temp : ", curr, left, right)

    # print(curr, start+1, start+left+1, inor[start+1:start+left+1])
    solve(start+1, start+left+1)
    # print(curr, end-right, end, inor[end-right:end])
    solve(end-right, end)

    print(curr)

def count(curr, start, end) :
    left = right = 0

    for i in range(start+1, end) :
        if inor[i] < curr :
            left += 1
        elif inor[i] > curr :
            right += 1

    return left, right

inor = []
while True :
    try :
        inor.append(int(input()))
    except :
        break

solve(0, len(inor))

file.close()