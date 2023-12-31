def find(num, parent):
    if parent[num] != num:
        parent[num] = find(parent[num], parent)
    return parent[num]


def union(a, b, parent):
    fa, fb = parent[a], parent[b]
    if fa < fb:
        parent[fb] = fa
    elif fa > fb:
        parent[fa] = fb


def solution(n, costs):
    answer = 0

    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: (x[-1]))

    for u, v, c in costs:
        if find(u, parent) != find(v, parent):
            union(u, v, parent)
            answer += c

    return answer


def main():
    answer = solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
    print(answer)


if __name__ == '__main__':
    main()