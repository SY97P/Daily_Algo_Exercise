def check(big_lock):
    n = len(big_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if big_lock[i][j] != 1:
                return False
    return True

def rotate(key):
    n = len(key)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = key[n-1-j][i]
    return result

def solution(key, lock):
    m, n = len(key), len(lock)
    big_lock = [[0] * (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            big_lock[i+n][j+n] = lock[i][j]
            
    for k in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        big_lock[x+i][y+j] += key[i][j]
                if check(big_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        big_lock[x+i][y+j] -= key[i][j]
    
    return False