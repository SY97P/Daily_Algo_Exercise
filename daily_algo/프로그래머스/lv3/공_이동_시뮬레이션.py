def solution(n, m, x, y, queries):
    sx, ex, sy, ey = x, x, y, y
    for op, dx in reversed(queries):
        if op == 0:  # 열 번호 감소 방향
            ey = min(m-1, ey+dx)
            if sy != 0:
                sy += dx
        elif op == 1:  # 열 번호 증가 방향
            sy = max(0, sy-dx)
            if ey != m-1:
                ey -= dx
        elif op == 2:  # 행 번호 감소 방향
            ex = min(n-1, ex+dx)
            if sx != 0:
                sx += dx
        else:  # 행 번호 증가 방향
            sx = max(0, sx-dx)
            if ex != n-1:
                ex -= dx

        if sx >= n or sy >= m or ex < 0 or ey < 0:
            return 0
    return (ex-sx+1)*(ey-sy+1)

def main():
    # answer = solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]])
    answer = solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]])
    print(answer)


main()
