# A
# --B
# ----C
# ------D
# --C
# B
# --A
#
# APPLE
# --APPLE
# --BANANA
# ----KIWI
# KIWI
# --APPLE
# --BANANA

import os

filename = "개미굴.txt"
file = open(os.getcwd() + "\\" + filename)

input = file.readline


class Node:
    def __init__(self, name):
        self.node = name
        self.children = []

    def find(self, item):
        index = -1
        for i, child in enumerate(self.children):
            if child.node == item:
                index = i
                break
        return index

    def sort(self):
        self.children.sort(key=lambda x: x.node)


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, items):
        curr_node = self.head

        for item in items:
            next_node_idx = curr_node.find(item)
            # child에 item을 추가해줘야함
            if next_node_idx == -1:
                curr_node.children.append(Node(item))
            curr_node = curr_node.children[next_node_idx]

    def print(self):
        dfs(self.head, 0)


def dfs(node, depth):
    node.sort()
    for child in node.children:
        print("--"*depth, end="")
        print(child.node)
        dfs(child, depth+1)


n = int(input())
trie = Trie()
for _ in range(n):
    line = input().strip().split()
    k = int(line[0])
    route = line[1:]
    trie.insert(route)

trie.print()


file.close()
