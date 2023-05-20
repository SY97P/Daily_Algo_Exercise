import os
file = open(os.getcwd()+"\암호문1.txt")

input = file.readline


def get_commands(m):
    commands = []
    temp = list(input().split())
    idx = 0
    while idx < len(temp):
        oper = temp[idx]
        x = int(temp[idx+1])
        y = int(temp[idx+2])
        idx += 3
        val = temp[idx:idx+y]
        idx += y
        if x >= BOUND:
            continue
        commands.append([x, val])
    return commands


BOUND = 10
for tc in range(1, 11):
    n = int(input())
    origin = list(input().split())[:BOUND]
    m = int(input())
    for s, v in get_commands(m):
        origin = origin[:s] + v + origin[s:]
        origin = origin[:BOUND]

    answer = ' '.join(origin)
    print(f'#{tc} {answer}')


file.close()