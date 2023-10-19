from collections import defaultdict


def solution(gems):
    n = len(gems)
    answer = [1, n]
    target = len(set(gems))
    dic = defaultdict(int)
    e = 0
    for s in range(n):
        while e < n and len(dic) < target:
            dic[gems[e]] += 1
            e += 1

        if len(dic) == target and answer[1]-answer[0] > e-(s+1):
            answer = [s + 1, e]

        dic[gems[s]] -= 1
        if dic[gems[s]] <= 0:
            del dic[gems[s]]

    return answer


def main():
    # answer = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
    # answer = solution(["AA", "AB", "AC", "AA", "AC"])
    answer = solution(["A"])
    print(answer)


if __name__ == '__main__':
    main()
