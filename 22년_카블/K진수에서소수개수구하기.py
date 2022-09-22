import math

def findPrime(num) :
    if num <= 1: 
        return False
    for i in range(2, int(math.sqrt(num)+1)) :
        if num % i == 0 :
            return False
    return True
    

def convert(n, k) :
    result = ""
    while n > k :
        result = str(n%k) + result
        n //= k
    result = str(n) + result
    return result

def solution(n, k):
    n_number = convert(n, k)
    num_list = n_number.split("0")
    answer = 0
    for num in num_list : 
        if num != "" and findPrime(int(num)) :
            # print(num, findPrime(int(num)))
            answer += 1
    return answer