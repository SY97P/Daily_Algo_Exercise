import heapq

def getBoth(box) : 
    return (heapq.nlargest(1, box)[0], box[0])

for tc in range(1, 11) : 
    dump = int(input())
    boxes = list(map(int, input().split()))
    heapq.heapify(boxes)
    
    count = 0
    
    largest, smallest = getBoth(boxes)
    
    while largest - smallest > 1 and count < dump : 
        heapq.heappop(boxes)
        boxes.remove(largest)
        heapq.heapify(boxes)
        
        #print(smallest, largest, largest - smallest)
        
        heapq.heappush(boxes, smallest + 1)
        heapq.heappush(boxes, largest - 1)
        
        count += 1
        
        largest, smallest = getBoth(boxes)
        
    result = getBoth(boxes)
    print("#%d %d" % (tc, result[0] - result[1]))