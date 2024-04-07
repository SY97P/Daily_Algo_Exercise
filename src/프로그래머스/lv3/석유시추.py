"""
문제요약

- 세로 n, 가로 m 격자 속에 있는 석유 덩이리 중에 단 하나만 시추할 때
- 가장 많은 석유를 뽑을 수 있는 시추관 위치 찾기
- 시추관은 열 하나를 관통하는 형태 (행으로는 뚫을 수 없음)
- 만약 시추관이 관통한 석유 덩어리는 모두 뽑을 수 있음

제한사항

- 1 <= n <= 500 (정확성 테스트 시 100)
- 1 <= m <= 500 (정확성 테스트 시 100)
- land[i][j]
    - 0 : 빈 땅
    - 1 : 석유 있는 땅

해결전략

- BFS 활용해 모든 석유 덩어리의 크기 구하기
- DP[i] : i 열에서 얻을 수 있는 석유 합
- 각 석유 덩어리가 포함하는 열에 해당하는 DP 값에 더해주기
- DP 값 중에서 최대 구하기
"""
from collections import deque

dp, visited = [], []
n, m = 0, 0
dlist = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def evaluate_oil(x, y, land):
    oil_amount = 1
    q = deque([(x, y)])

    cols = {y}

    while q:
        i, j = q.popleft()

        for dx, dy in dlist:
            di, dj = i + dx, j + dy
            if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and land[di][dj]:
                visited[di][dj] = True
                oil_amount += 1
                cols.add(dj)
                q.append((di, dj))

    for col in cols:
        dp[col] += oil_amount


def solution(land):
    global dp, visited, n, m

    n, m = len(land), len(land[0])
    dp = [0] * m

    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                visited[i][j] = True
                evaluate_oil(i, j, land)

    return max(dp)


def main():
    # 9
    answer = solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])
    print(answer)

    # 16
    answer = solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])
    print(answer)


if __name__ == '__main__':
    main()
