import sys

sys.setrecursionlimit(10**6)


# 전위 순회 : T L R
def preorder(nodeinfo):
    if not nodeinfo:
        return []
    root = nodeinfo[0]
    l = [node for node in nodeinfo if root[1] > node[1]]
    r = [node for node in nodeinfo if root[1] < node[1]]
    return [root[0]] + preorder(l) + preorder(r)


# 후위 순회 : L R T
def postorder(nodeinfo):
    if not nodeinfo:
        return []
    root = nodeinfo[0]
    l = [node for node in nodeinfo if root[1] > node[1]]
    r = [node for node in nodeinfo if root[1] < node[1]]
    return postorder(l) + postorder(r) + [root[0]]


def solution(nodeinfo):
    answer = []

    nodeinfo = [[(idx + 1), node[0], node[1]] for idx, node in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[2], x[1], x[0]))

    answer.append(preorder(nodeinfo))
    answer.append(postorder(nodeinfo))

    return answer


def main():
    answer = solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
    print(answer)


if __name__ == '__main__':
    main()
