from collections import deque

def solution(queue1, queue2) : 
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    answer = 0 
    mid = sum(queue1)
    goal = (mid + sum(queue2)) / 2
    loop_limit = len(queue1) * 4
    
    if goal - int(goal) != 0 :
        return -1
    
    while mid != goal : 
        if not queue1 or not queue2 : 
            return -1
        
        if mid < goal : 
            item = queue2.popleft()
            queue1.append(item)
            mid += item
        else : 
            item = queue1.popleft()
            queue2.append(item)
            mid -= item
        answer += 1
        if answer > loop_limit : 
            return -1
        
    return answer