# 2
# 2
# 1
# 10
#
# 4000
# 4000
# 4000
# 0
#
# -2
# -2
# -1
# 2
#
# 0
# 0
# 0
# 1

file = open("./통계학.txt")

input = file.readline

BOUND = 4000

n = int(input())
alist = [0 for _ in range(BOUND*2+1)]
for _ in range(n):
    alist[int(input())+BOUND] += 1

sumof = 0
value = idx = 0
freq_val, freq_max, freq_count = 0, 0, 0
minVal, maxVal = float('inf'), -float('inf')

for i in range(BOUND*2+1):
    if alist[i] != 0:
        sumof += (i-BOUND) * alist[i]
        if idx <= n//2:
            idx += alist[i]
            value = i-BOUND
        if freq_max <= alist[i]:
            if freq_max == alist[i]:
                if freq_count < 1:
                    freq_count += 1
                    freq_max = alist[i]
                    freq_val = i - BOUND
            else:
                freq_max = alist[i]
                freq_val = i - BOUND
                freq_count = 0
        minVal = min(minVal, i-BOUND)
        maxVal = max(maxVal, i-BOUND)

print(round(sumof / n))
print(value)
print(freq_val)
print(maxVal - minVal)


file.close()