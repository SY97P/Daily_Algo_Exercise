from collections import defaultdict 

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    report_dict = defaultdict(set)
    for r in report : 
        a, b = r.split()
        report_dict[b].add(a)
        
    for key in report_dict.keys() :
        # print(key, report_dict[key], len(report_dict[key]))
        if len(report_dict[key]) >= k : 
            for reporter in report_dict[key] :
                answer[id_list.index(reporter)] += 1
            
    
    return answer