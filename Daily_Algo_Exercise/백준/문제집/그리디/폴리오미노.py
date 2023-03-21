# AAAABB
# BB.BB
# -1
# -1
# BB.AAAAAAAABB..AAAAAAAA...AAAABB

file = open("./폴리오미노.txt")

input = file.readline

a, b = "AAAA", "BB"

for _ in range(5):
    board = input().strip()
    n = len(board)
    i = 0
    result = ""
    while i < n:
        if board[i] == ".":
            result += "."
            i += 1
            continue
        if i+3 < n and board[i+1] != "." and board[i+2] != "." and board[i+3] != ".":
            result += a
            i += 4
            continue
        if i+1 < n and board[i+1] != ".":
            result += b
            i += 2
            continue
        result = -1
        break
    print(result)

file.close()