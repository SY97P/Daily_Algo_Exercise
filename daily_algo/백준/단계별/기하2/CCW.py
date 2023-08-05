# -1
# 0
# 1

file = open("./CCW.txt")

input = file.readline

x, y = [], []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

xr, yr = 0, 0
for i in range(3):
    xr += x[i] * y[i+1]
    yr += y[i] * x[i+1]

outer_product = (xr - yr)

if outer_product == 0:
    print(0)
elif outer_product < 0:
    print(1)
else:
    print(-1)

file.close()