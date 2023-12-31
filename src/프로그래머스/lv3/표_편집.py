class Point:
    def __init__(self, prev, post, n):
        self.prev = prev if prev >= 0 else None
        self.post = post if post < n else None


def solution(n: int, k: int, cmds: list) -> str:
    answer = ['O'] * n
    pointer = k
    stack = []
    links = [Point(i - 1, i + 1, n) for i in range(n)]

    for cmd in cmds:
        line = cmd.split()
        op, dx = line[0], None if len(line) < 2 else int(line[1])
        if op == 'U':
            cnt = 0
            while links[pointer].prev is not None and cnt < dx:
                cnt += 1
                pointer = links[pointer].prev
        elif op == 'D':
            cnt = 0
            while links[pointer].post is not None and cnt < dx:
                cnt += 1
                pointer = links[pointer].post
        elif op == 'C':
            answer[pointer] = 'X'
            stack.append(pointer)
            if links[pointer].prev is not None:
                links[links[pointer].prev].post = links[pointer].post
            if links[pointer].post is not None:
                links[links[pointer].post].prev = links[pointer].prev
                pointer = links[pointer].post
            else:
                pointer = links[pointer].prev
        else:
            recover = stack.pop()
            answer[recover] = 'O'
            if links[recover].prev is not None:
                links[links[recover].prev].post = recover
            if links[recover].post is not None:
                links[links[recover].post].prev = recover

    return ''.join(answer)


def main():
    # answer = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
    answer = solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
    # answer = solution(5, 0, ["C", "C", "C", "C", "C"])
    print(answer)


if __name__ == '__main__':
    main()
