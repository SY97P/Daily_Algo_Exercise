# 전체 사용자 목록, 불량 사용자 마스킹 목록이 주어졌을때 가능한 모든 불량 사용자 목록 수를 구하는 문제
# 1. 불량 사용자 마스킹 목록 row 수 만큼 전체 사용자 목록을 순열 조합하기
# 2. 사용자 순열 조합과 불량 사용자 마스킹 목록 비교하기
#     2.1 길이 비교하기
#     2.2 와일드카드 '*' 제외하고 나머지 글자 일치여부 확인하기
# 3. 모두 일치한다면 answer 집합에 사용자 순열 조합에 정렬 + 문자열화 해서 넣기
# 4. answer 크기 반환하기

from itertools import permutations


def matched(can, ban):
    if len(can) != len(ban):
        return False
    for i in range(len(ban)):
        if ban[i] == '*':
            continue
        elif can[i] != ban[i]:
            return False
    return True


def all_matched(candidate, banned_id):
    for i in range(len(banned_id)):
        if not matched(candidate[i], banned_id[i]):
            return False
    return True


def solution(user_id, banned_id):
    answer = set()

    for candidate in permutations(user_id, len(banned_id)):
        if all_matched(candidate, banned_id):
            candidate = sorted(list(candidate))
            answer.add(''.join(candidate))

    return len(answer)


def main():
    answer = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
    print(answer)


if __name__ == '__main__':
    main()
