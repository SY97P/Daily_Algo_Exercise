# 1. 시간 기준으로 이분탐색
# 2. 추정 시간 동안 각 도시에서 구할 수 있는 광물(금, 은, 총량) 구하기
# 3. 얻은 광물이 목표치에 맞는지 확인
# 4.1 목표치에 크거나 같으면 보다 적은 시간 기준으로 다시 이분탐색
# 4.2 목표치보다 적으면 보다 큰 시간 기준으로 다시 이분탐색

def mining_all_cities(m, g, s, w, t):
    n = len(t)
    gold, silver, total = 0, 0, 0
    # 시간 기준 각 도시 별 운송 가능 횟수
    cnt = [m//(t[i]*2) for i in range(n)]
    for i in range(n):
        if m >= cnt[i]*2*t[i]+t[i]:
            cnt[i] += 1
    for i in range(n):
        mine = min(w[i]*cnt[i], g[i]+s[i])
        total += mine
        gold += min(mine, g[i])
        silver += min(mine, s[i])
    return gold, silver, total

# @param a : 필요한 금
# @param b : 필요한 은
# @param g : 도시별 금 보유량
# @param s : 도시별 은 보유량
# @param w : 도시별 트럭 수용량
# @param t : 도시별 트럭 편도 소모 시간
def solution(a, b, g, s, w, t):
    answer = -1
    # 최악의 경우
    l, r = 0, 1e15
    while l <= r:
        m = (l + r) // 2
        gold, silver, total = mining_all_cities(m, g, s, w, t)
        if gold >= a and silver >= b and total >= a + b:
            answer = m
            r = m - 1
        else:
            l = m + 1
    return answer


def main():
    answer = solution(10, 10, [100], [100], [7], [10])
    print(answer)


main()
