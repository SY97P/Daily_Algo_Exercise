def fib_recursion(n) :
	global count1
	
	if (n == 1 or n == 2) :
		return 1
	count1 += 1
	return fib_recursion(n-1) + fib_recursion(n-2)

def fib_dp(n) : 
	global count2

	fib = [1, 1]

	for i in range(2, n) : 
		fib.append(fib[i-1] + fib[i-2])
		count2 += 1

	return fib[n-1]
	

def main() :
	global count1, count2
	
	# n = int(input())
	n = 30

	f = [1, 1]
	
	print(fib(n))

main()

# 실제 제출 코드
# n = int(input())
# count = 0

# def fib(n) : 
#     global count
    
#     if (n == 1 or n == 2) :
#         return 1
#     count += 1
#     return fib(n - 1) + fib(n - 2)

# fib(n)
# print(count, n - 2)