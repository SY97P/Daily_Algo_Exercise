# 2.00
# 1.67
# 2.71

file = open('./휴대폰자판.txt', "r")

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
        count = 1
        for t in token:
            btn_clicked = False
            if curr_node.data is not None or (curr_node.node is not None and len(curr_node.children) > 1):
                btn_clicked = True
            curr_node = curr_node.children[t]
            if btn_clicked:
                count += 1
        #     print(t, count)
        # print(token, count)
        return count


while True:
    try:
        n = int(input())
        trie = Trie()
        count = 0
        tokens = [input().strip() for _ in range(n)]
        for token in tokens:
            trie.insert(token)
        for token in tokens:
            count += trie.find(token)
        print("%.2f" % (count / n))
    except EOFError or ValueError:
        break


file.close()