'''
문제요약

- n * m 퍼즐판
- 빨간/파란 수레가 각각의 시작칸에서 도착 칸까지 모두 이동시킬 때 필요한 최소 턴 수 구하기
- 퍼즐을 풀 수 없는 경우 0 반환
- 각 턴마다 반드시 모든 수레를 상하좌우 인접 한 칸으로 이동시켜야 함
    - 벽, 퍼즐 바깥으로 이동 불가
    - 재방문 불가
    - 도착칸에 도달하면 움직이지 않음
    - 동시에 같은 칸에 수레가 있을 수 없음
    - 수레끼리 자리를 바꿀 수 없음

제한사항

- 1 <= 퍼즐 가로, 세로 <= 4
- 각 퍼즐 값
    - 0 : 빈 칸
    - 1 ; 빨간 수레 시작 칸
    - 2 : 파란 수레 시작 칸
    - 3 : 빨간 수레 도착 칸
    - 4 : 파란 수레 도착 칸
    - 5 : 벽

해결전략 (백트래킹)

- 각 라운드 별로 빨강, 파랑을 인접 한 칸으로 이동
    - 다음 칸 구하기
        - bound, 벽 검사 -> out of index, maze[i][j] = 5?
        - 재방문 검사 -> visited
    - 다음 칸 연산하기
        - 도착칸 도달 검사 -> 해당 수레 멈추기
        - 동시에 같은 수레 이동 red == blue -> x
        - 수레끼리 자리 바꿀 수 없음
            - next_red = blue and next_blue = red -> X
'''

n, m = 0, 0
maze = []
r_visited, b_visited = [], []
t_red, t_blue = None, None
dlist = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def get_point(key):
    for i in range(n):
        for j in range(m):
            if maze[i][j] == key:
                return Point(i, j)
    return Point(-1, -1)


def get_next(point, visited):
    next_point = []
    for dx, dy in dlist:
        nx, ny = point.x + dx, point.y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] != 5:
            next_point.append(Point(nx, ny))
    return next_point


def dfs(red, blue, turn):
    if red == t_red and blue == t_blue:
        return turn

    next_red = get_next(red, r_visited) if red != t_red else [red]
    next_blue = get_next(blue, b_visited) if blue != t_blue else [blue]

    result = 1e9

    for n_red in next_red:
        for n_blue in next_blue:
            if n_red == n_blue or (n_red == blue and n_blue == red):
                continue
            r_visited[n_red.x][n_red.y] = True
            b_visited[n_blue.x][n_blue.y] = True
            result = min(result, dfs(n_red, n_blue, turn + 1))
            r_visited[n_red.x][n_red.y] = False
            b_visited[n_blue.x][n_blue.y] = False

    return result


def solution(_maze):
    global n, m, maze, t_red, t_blue, r_visited, b_visited

    maze = _maze
    n, m = len(maze), len(maze[0])
    red, blue = get_point(1), get_point(2)
    t_red, t_blue = get_point(3), get_point(4)
    r_visited = [[False for _ in range(m)] for _ in range(n)]
    b_visited = [[False for _ in range(m)] for _ in range(n)]
    r_visited[red.x][red.y] = True
    b_visited[blue.x][blue.y] = True

    answer = dfs(red, blue, 0)

    return answer if answer < 1e9 else 0


def main():
    # 3
    answer = solution([[1, 4], [0, 0], [2, 3]])
    print(answer)

    # 7
    answer = solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]])
    print(answer)

    # 0
    answer = solution([[1, 5], [2, 5], [4, 5], [3, 5]])
    print(answer)

    # 0
    answer = solution([[4, 1, 2, 3]])
    print(answer)


if __name__ == '__main__':
    main()
