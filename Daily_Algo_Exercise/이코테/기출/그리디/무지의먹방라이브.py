food_times = [3, 1, 2]
k = 5


import heapq

n = len(food_times)
q = []
for i in range(n):
	heapq.heappush(q, (food_times[i], i+1))

curr_time = 0
prev_food = 0

while curr_time + (q[0][0] - prev_food) * n <= k:
	now_food, now_index = heapq.heappop(q)
	curr_time += (now_food - prev_food) * n
	prev_food = now_food 
	n -= 1

result = sorted(q, key=lambda x: x[1])
print(result[(k-curr_time)%n][1])