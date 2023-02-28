file = open("./문자열집합.txt", "w")

import random

n = random.randint(1, 10**4)
m = random.randint(1, 10**4)

file.write(str(n)+" "+str(m)+"\n")

for _ in range(n):
    token = ''.join([random.choice([chr(ord('a')+i) for i in range(26)]) for _ in range(random.randint(1, 500))])
    file.write(token+"\n")

for _ in range(m):
    token = ''.join([random.choice([chr(ord('a')+i) for i in range(26)]) for _ in range(random.randint(1, 500))])
    file.write(token+"\n")

file.close()