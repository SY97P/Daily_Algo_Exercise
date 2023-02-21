# 1
# 16

path = "../백준/단계별/문자열알고리즘1/찾기.txt"
file = open(path, "r")

input = file.readline

# * KMP
# 1. 문자열 T, P를 strip 함수를 피휘해서 입력받기
# 2. P의 j인덱스 글자가 이전에 어느 위치에서 출현했는지 기록하는 리스트 생성
# 3. T와 P를 비교해서 KMP 알고리즘 완성

def get_pi(p, l):
    pi = [0 for _ in range(l)]
    j = 0
    for i in range(1, l):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(m, l):
    count = 0
    loc = []

    j = 0
    for i in range(m):
        # print(i, t[i], j, p[j])
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
            # print("rollback : ", i, t[i], j, p[j])
        if t[i] == p[j]:
            j += 1
            if j == l:
                j = pi[j-1]
                count += 1
                loc.append(i-l+2)
                # print(i, t[i], j, p[j], l, loc)

    print(count)
    print(*loc)


t = list(input().replace('\n', ''))
p = list(input().replace('\n', ''))

pi = get_pi(p, len(p))

# print(pi)

kmp(len(t), len(p))


file.close()
