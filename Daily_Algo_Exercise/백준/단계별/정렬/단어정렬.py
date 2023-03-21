# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate

file = open("./단어정렬.txt")

input = file.readline

n = int(input())
words = {input().strip() for _ in range(n)}
words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)

file.close()