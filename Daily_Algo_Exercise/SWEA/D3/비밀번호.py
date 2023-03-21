#1 1234
#2 4123
#3 123123
#4 1234123123
#5 12341
#6 123535
#7 123432141
#8 231231321
#9 12312323
#10 9823

file = open("./SWEA/D3/비밀번호.txt", "r")

input = file.readline

for tc in range(1, 11) : 
	n, text_origin = input().split()

	text = text_origin
	length = int(n)

	index = 0 
	while index < length - 1 : 
		i = index
		j = i + 1
		eraze = False
		while 0 <= i and j < length and text[i] == text[j] : 
			i -= 1
			j += 1
			eraze = True
		if eraze :
			text = text[:i+1] + text[j:]
			length -= j - i - 1
			index = i
		else : 
			index += 1

	print("#%d %s" %(tc, text))
		
file.close()