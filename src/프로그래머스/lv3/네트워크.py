def find(node, parent):
    if node != parent[node]:
        parent[node] = find(parent[node], parent)
    return parent[node]


def union(a, b, parent):
    fa, fb = find(a, parent), find(b, parent)
    if fa < fb:
        parent[fb] = fa
    elif fa > fb:
        parent[fa] = fb


def solution(n, computers):
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(i):
            if computers[i][j] == 1:
                if find(i, parent) != find(j, parent):
                    union(i, j, parent)

    return len(set([find(node, parent) for node in parent]))


def main():
    answer = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(answer)


if __name__ == '__main__':
    main()
