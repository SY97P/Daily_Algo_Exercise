def solution(routes):
    answer = 1

    routes = sorted(routes, key=lambda x: (x[1], x[0]))

    point = routes[0][1]

    for s, e in routes:
        if point < s:
            point = e
            answer += 1

    return answer


def main():
    answer = solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])
    print(answer)


if __name__ == '__main__':
    main()