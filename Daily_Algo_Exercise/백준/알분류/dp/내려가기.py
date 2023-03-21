# 18 6
# 0 0

file = open("./백준/알분류/dp/내려가기.txt")

input = file.readline 


def main():
	for _ in range(1):
		n = int(input())
	
		max_dp = [0 for _ in range(3)]
		min_dp = [0 for _ in range(3)]

		for k in range(n):
			curr = list(map(int, input().split()))
			if k == 0:
				for i in range(3):
					max_dp[i] = curr[i]
					min_dp[i] = curr[i]
				continue 
			max_temp = []
			min_temp = []
			for i in range(3):
				max_val = -float('inf')
				min_val = float('inf')
				for j in range(-1, 2):
					if 0 <= i + j < 3:
						max_val = max(max_val, max_dp[i+j])
						min_val = min(min_val, min_dp[i+j])
				max_temp.append(curr[i] + max_val)
				min_temp.append(curr[i] + min_val)
			max_dp, min_dp = max_temp, min_temp
		print(max(max_dp), min(min_dp))


if __name__ == '__main__':
	main()
	

file.close()