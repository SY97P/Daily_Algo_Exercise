# icpc 2
# spc 2
# txt 3
# world 1

file = open("./Daily_Algo_Exercise/백준/문제집/구현/파일정리.txt")

input = file.readline 

from collections import defaultdict

n = int(input())

dic = defaultdict(int)

for _ in range(n):
	extension = input().strip().split(".")[1]
	dic[extension] += 1

key_list = list(dic.keys())
key_list.sort()
for key in key_list:
	print(key, dic[key])


file.close()