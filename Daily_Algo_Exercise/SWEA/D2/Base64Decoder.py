#1 Life itself is a quotation.
#2 Suspicion follows close on mistrust.
#3 To doubt is safer than to be secure.
#4 Only the just man enjoys peace of mind.
#5 A full belly is the mother of all evil.
#6 A gift in season is a double favor to the needy.
#7 Books are ships which pass through the vast seas of time.
#8 Let thy speech be short, comprehending much in few words.
#9 The world is a beautiful book, but of little use to him who cannot read it.
#10 He who spares the rod hates his son, but he who loves him is careful to discipline him.

file = open("./SWEA/D2/Base64Decoder.txt", "r")

input = file.readline

decoder = [chr(i) for i in range(65, 91)]
for i in range(97, 123) : 
	decoder.append(chr(i))
for i in range(10) : 
	decoder.append(str(i))
decoder.append('+')
decoder.append('/')

t = int(input())

for tc in range(1, t + 1) : 
	line = input().strip()
	
	res = ""

	for l in line : 
		num = bin(decoder.index(l))[2:]

		while len(num) < 6 : 
			num = '0' + num

		res += num

	result = ""
	for i in range(0, len(res), 8) :
		curr = int(res[i:i+8], 2)
		result += chr(curr)

	print("#%d %s" % (tc, result))

file.close()