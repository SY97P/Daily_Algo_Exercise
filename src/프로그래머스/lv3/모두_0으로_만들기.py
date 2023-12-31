import sys

sys.setrecursionlimit(10 ** 6)


def solution(a, edges):
    n = len(a)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * n
    visited[0] = True

    def solve(node):
        w, c = a[node], 0
        for next_node in adj[node]:
            if not visited[next_node]:
                visited[next_node] = True
                rtn = solve(next_node)
                w += rtn[0]
                c += rtn[1]
        return w, abs(w)+c

    answer = solve(0)
    return answer[1] if answer[0] == 0 else -1


def main():
    # answer = solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])
    # answer = solution([0, 1, 0], [[0, 1], [1, 2]])
    # answer = solution([-1, 0, 1], [[0, 1], [1, 2]])
    # answer = solution([0, 0], [[0, 1]])
    answer = solution([-1, 1], [[0, 1]])
    print(answer)


if __name__ == '__main__':
    main()
