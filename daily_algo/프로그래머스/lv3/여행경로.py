def dfs(visited, path, tickets):
    if False not in visited:
        return path
    rtn = []
    for idx, (s, d) in enumerate(tickets):
        if rtn:
            continue
        if path[-1] == s and not visited[idx]:
            visited[idx] = True
            rtn = dfs(visited, path + [d], tickets)
            visited[idx] = False
    return rtn


def solution(tickets):
    answer = []

    tickets.sort()

    for idx, (s, d) in enumerate(tickets):
        if answer:
            continue
        if s == 'ICN':
            visited = [False] * len(tickets)
            visited[idx] = True
            answer = dfs(visited, [s, d], tickets)

    return answer

def main():
    # answer = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
    answer = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
    print(answer)


if __name__ == '__main__':
    main()