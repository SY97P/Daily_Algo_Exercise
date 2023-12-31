def solution(record) : 
	temp = []
	users = dict()

	for r in record : 
		if r.count(" ") > 1 : 
			action, id, name = r.split(" ")
			# print("a : ", action, "id : ", id, "n : ", name)
			users[id] = name
		else : 
			action, id = r.split(" ")
			name = ""
			# print("a : ", action, "id : ", id)

		# print(users)
		
		if action == "Enter" : 
			temp.append([" 들어왔습니다.", id])
		elif action == "Leave" : 
			temp.append([" 나갔습니다.", id])
		

		# print(answer)

	answer = []
	for t in temp : 
		answer.append(users[t[1]] + "님이" + t[0])

	# print(answer)
	return answer
		
		
			

def main() : 
	record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
	# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
	print("solution : ", solution(record))

main()