def get_next_loc(loc, board):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        next = (loc[0] + dx, loc[1] + dy)
        if next in board:
            yield *next, loc[-1]

def dfs(aloc, bloc, board, step):
    next_loc = list(get_next_loc(aloc, board))
    if not next_loc or aloc[:2] not in board:
        return False, step

    rtns = [dfs(bloc, next, board - {next[:2]}, step + 1) for next in next_loc]
    wins = [rtn[1] for rtn in rtns if not rtn[0]]
    loses = [rtn[1] for rtn in rtns if rtn[0]]

    if wins:
        return True, min(wins)
    else:
        return False, max(loses)

def solution(brd, aloc, bloc):
    n, m = len(brd), len(brd[0])
    board = {(r, c) for r, row in enumerate(brd) for c, col in enumerate(row) if col}
    return dfs(tuple(aloc + [0]), tuple(bloc + [1]), board, 0)[1]

answer = solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])
print(answer)