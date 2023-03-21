# 4

file = open("./문자열집합.txt", "r")

input = file.readline


class TrieNode:
    def __init__(self, node, data=None):
        self.node = node
        self.data = data
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, token):
        curr_node = self.root

        for t in token:
            if t not in curr_node.children:
                curr_node.children[t] = TrieNode(t)
            curr_node = curr_node.children[t]

        curr_node.data = token

    def find(self, token):
        curr_node = self.root

        for t in token:
            if t not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[t]

        return curr_node.data is not None


n, m = map(int, input().split())
trie = Trie()
count = 0
for _ in range(n):
    token = input().strip()
    trie.insert(token)
for _ in range(m):
    token = input().strip()
    if trie.find(token):
        count += 1
print(count)


file.close()