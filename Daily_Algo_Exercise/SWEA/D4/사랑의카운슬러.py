import os

file = open(os.getcwd() + "\사랑의카운슬러.txt")

input = file.readline


def main():
    global answer
    t = int(input())
    for tc in range(1, t + 1):
        answer = 1e11
        n = int(input())
        worms = [list(map(int, input().split())) for _ in range(n)]
        visited = [False] * len(worms)

        def min_vec():
            global answer
            move_worms = [0, 0]
            wait_worms = [0, 0]
            for i, (x, y) in enumerate(worms):
                if visited[i]:
                    move_worms[0] += x
                    move_worms[1] += y
                else:
                    wait_worms[0] += x
                    wait_worms[1] += y
            answer = min(answer, (wait_worms[0] - move_worms[0]) ** 2 + (wait_worms[1] - move_worms[1]) ** 2)

        def combinations(idx, cnt):
            # 이동하는 지렁이만 구하면
            # 나머지는 이동하지 않고 오기를 기다리는 지렁이가 되므로, trunning이 가능함.
            if cnt == n // 2:
                min_vec()
                return
            # 모든 순서쌍(순열)에 대해서 연산하면 중복 연산이 발생함.
            # 따라서 중복제거를 위해서 조합으로 풀어야 함.
            for i in range(idx, len(worms)):
                visited[i] = True
                combinations(i + 1, cnt + 1)
                visited[i] = False

        combinations(0, 0)
        print(f'#{tc} {answer}')


if __name__ == '__main__':
    main()

file.close()
