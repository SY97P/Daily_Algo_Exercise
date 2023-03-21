file = open("./SWEA/D2/Base64Decoder.txt", "r")

from base64 import b64decode

t = int(input())

for tc in range(1, t + 1) : 
	line = input()
	result = b64decode(line).decode('UTF-8')
	print("#{} {}".format(tc, result))

file.close()