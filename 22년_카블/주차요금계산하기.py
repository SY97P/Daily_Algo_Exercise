from collections import defaultdict
import math

def makeFees(time, fees) : 
    default_time, default_cost, time_unit, cost_unit = fees
    if time <= default_time : 
        return default_cost
    time -= default_time
    return default_cost + cost_unit * math.ceil(time / time_unit)

def convert(time) :
    hour, minu = map(int, time.split(":"))
    return hour * 60 + minu

def solution(fees, records):
    time_dict = defaultdict(int)
    answer = defaultdict(int)
    for r in records : 
        time, num, note = r.split()
        # print(num, answer[num])
        if note == "IN" :
            time_dict[num] = convert(time)
            # print("num : ", num, "in_time : ", time_dict[num])
        else : 
            answer[num] += convert(time) - time_dict[num]
            # print("num : ", num, "during : ", answer[num])
            time_dict[num] = -1
    
    # count not getting out yet cars
    for key in time_dict.keys() :
        print(key, time_dict[key])
        if time_dict[key] != -1 :
            answer[key] += convert("23:59") - time_dict[key]
            time_dict[key] = 0
    
    for key in answer.keys() : 
        answer[key] = makeFees(answer[key], fees)
        
    lst = list(answer.keys())
    lst.sort()
    answer_lst = []
    for l in lst : 
        answer_lst.append(answer[l])
    return answer_lst