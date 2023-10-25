from heapq import heappush, heappop


def get_diff_cnt(node, word):
    cnt = 0
    for i in range(len(node)):
        if node[i] != word[i]:
            cnt += 1
            if cnt > 1:
                break
    return cnt


def solution(begin, target, words):
    answer = 51

    dp = {word: 1e9 for word in words}
    dp[begin] = 0
    dp[target] = 1e9

    q = [(0, begin)]

    while q:
        cnt, node = heappop(q)
        if dp[node] < cnt:
            continue
        if node == target:
            continue
        for word in words:
            if get_diff_cnt(node, word) == 1 and dp[word] > cnt + 1:
                dp[word] = cnt + 1
                heappush(q, (dp[word], word))

    return dp[target] if dp[target] < 1e9 else 0


def main():
    answer = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print(answer)


if __name__ == '__main__':
    main()
