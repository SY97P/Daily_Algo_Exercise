t = int(input())
for tc in range(1, t + 1) : 
    line = list(map(int, input().split()))
    answer = 0
    for l in line : 
        if l % 2 != 0 : 
            answer += l
    #print("#{0} {1}".format(tc, answer))
    print('#%d %d' % (tc, answer))