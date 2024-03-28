"""
문제요약

- 뽑는 순서가 정해져 있는 n개 카드뭉치
- 카드와 1:1 교환 가능한 coin 개 동전
- 처음 n/3 장의 카드 가지기 (n 은 6의 배수)
- 각 라운드 마다 카드 두 장 뽑기
    - 뽑은 카드는 동전을 소모해서 가지거나
    - 동전을 소모하지 않고 버릴 수 있음
- 합이 n+1 이 되도록 손패 두 장을 내고 다음 라운드 진행
- 손패 두 장 낼 수 없으면 게임 종료
- 카드뭉치에 남은 카드 없으면 게임 종료
- 게임에서 도달 가능한 최대 라운드 수 구하기

제한사항

- 0 <= coin <= n
- 6 <= n (6의 배수) < 1_000
- 1 <= 카드 값 <= n
- 카드값은 중복되지 않음

해결전략

1. n/3개 카드를 미리 손패로 가짐 -> 카드뭉치는 그만큼 제거
2. 라운드마다 두 장씩 카드뭉치에서 뽑기 (draws) -> 뽑은 카드는 모두 모아두기
    2.1 손패로만 목표합 가능 -> 손패 제거
    2.2 coin 하나 이상 and 손패 하나 + 뽑은 카드 하나로 목표합 가능 -> 손패 제거 + 뽑은 카드 제거 + 1 coin 제거
    2.3 coin 둘 이상 and 뽑은 카드 두개로 목표합 가능 -> 뽑은 카드 제거 + 2 coin 제거
3. 현재 라운드에서 아무것도 내지 못하거나 (라운드 클리어 X) or 남은 카드뭉치가 없는 경우
"""

from collections import deque


def solution(coin, cards):
    answer = 1

    n = len(cards)
    target = n + 1

    hands = cards[:n // 3]
    cards = deque(cards[n // 3:])
    draws = deque()

    while cards:
        draws += [cards.popleft(), cards.popleft()]

        round_clear = False

        for hand in hands:
            if target - hand in hands:
                round_clear = True
                hands.remove(hand)
                hands.remove(target - hand)
                break

        if not round_clear and coin >= 1:
            for draw in draws:
                for hand in hands:
                    if draw + hand == target:
                        coin -= 1
                        round_clear = True
                        draws.remove(draw)
                        hands.remove(hand)
                        break
                if round_clear:
                    break

        if not round_clear and coin >= 2:
            for draw in draws:
                if target - draw in draws:
                    coin -= 2
                    round_clear = True
                    draws.remove(draw)
                    draws.remove(target - draw)
                    break

        if round_clear:
            answer += 1
            continue
        return answer

    return answer


def main():
    # 5
    answer = solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
    print(answer)

    # 2
    answer = solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12])
    print(answer)

    # 4
    answer = solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7])
    print(answer)

    # 1
    answer = solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    print(answer)


if __name__ == '__main__':
    main()