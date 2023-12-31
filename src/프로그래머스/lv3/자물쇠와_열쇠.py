def get_lock(lock, n):
    new_lock = [[0] * 3 * n for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    return new_lock


def print_lock(board):
    for b in board:
        print(b)
    print()


def rollback(x, y, lock, key, n, m):
    for i in range(m):
        for j in range(m):
            lock[x + i][y + j] -= key[i][j]


def unlocking(x, y, lock, key, n, m):
    for i in range(m):
        for j in range(m):
            lock[x + i][y + j] += key[i][j]
    for i in range(n):
        for j in range(n):
            if lock[n + i][n + j] != 1:
                rollback(x, y, lock, key, n, m)
                return False
    rollback(x, y, lock, key, n, m)
    return True


def rotate_key(key):
    return list(zip(*key[::-1]))


def solution(key, lock):
    n, m = len(lock), len(key)
    lock = get_lock(lock, n)

    for i in range(2 * n):
        for j in range(2 * n):
            for _ in range(4):
                key = rotate_key(key)
                if unlocking(i, j, lock, key, n, m):
                    return True

    return False


def main():
    answer = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    print(answer)


if __name__ == '__main__':
    main()
