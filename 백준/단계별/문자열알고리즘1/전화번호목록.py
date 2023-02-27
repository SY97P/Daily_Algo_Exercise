# YES
# NO
# NO 
# YES

import os
filename = "전화번호목록.txt"
file = open(os.getcwd()+"\\"+filename, "r")

input = file.readline


# * Trie 자료구조
# - 문자열 검색 최적화 알고리즘 (문자열 집합 판별 알고리즘)
# - 좋은 시간복잡도 but, 안 좋은 공간복잡도
# - 배열 / 리스트 : O(m), map : O(m log n)
# - 공간복잡도 : O(m*n^2)
# - 메모리 제한이 빡빡할 경우 시간성능을 조금 포기해서 맵 자료구조를 이용한 구조로 변경

# Node 클래스 
# param
# node : 현재 노드(문자열을 이루는 문자 하나 혹은 부분 분자열)
# data : 현재 노드가 문자열의 마지막인지 기록 (문자열의 마지막일 경우 원본 문자열 전체가 기록됨)
# children : 자식노드
class Node:
    def __init__(self, node, data=None):
        self.node = node
        self.data = data
        self.children = dict()


# Trie 클래스
# head : 의미 없이 허상으로 존재하는 root 노드 (node, data = None /null)
# insert 메소드 : 문자열을 트라이 구조에 추가
# 	-> 부분문자열(prefix)가 일치할 경우 일치하는 prefix 노드까지 이동한 후에 다시 비교
# 	-> prefix와 현재 문자열이 일치하지 않을 경우 현재 노드의 children에 추가
# 	-> 모든 문자열 추가 후 문자열의 마지막에 해당하는 노드의 data 멤버변수 갱신
# find 메소드 : 문자열이 트라이 구조에 있는지 여부 반환
#   -> 모든 문자열을 비교했음에도 해당 노드의 data가 None일 경우 문자열의 끝까지 도달한 것이 아니므로, 찾는 문자열이 아닐 수 있음.
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, digits):
        curr_node = self.head

        for digit in digits:
            if digit not in curr_node.children:
                curr_node.children[digit] = Node(digit)
            curr_node = curr_node.children[digit]

        curr_node.data = digits

    #
    def find(self, digits):
        curr_node = self.head

        for digit in digits:
            if digit not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[digit]
                if curr_node.data != None and curr_node.data != digits:
                    return True
        return False

    def print(self):
        dfs(self.head, 0)


def dfs(node, depth):
    for child_key in node.children.keys():
        next_node = node.children[child_key]
        print("--" * depth, end="")
        print(next_node.node, next_node.data)
        dfs(next_node, depth + 1)


t = int(input())

for tc in range(t):
    n = int(input())
    trie = Trie()
    consistancy = True
    digits_list = []
    for _ in range(n):
        digits = input().strip()
        digits_list.append(digits)
        trie.insert(digits)
    for digits in digits_list:
        if trie.find(digits):
            consistancy = False
            break

    if consistancy:
        print("YES")
    else:
        print("NO")

file.close()
