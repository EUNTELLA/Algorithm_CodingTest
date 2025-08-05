t = int(input())


for _ in range(t):
    n = int(input())
    arr=[]
    for i in range(n):
        doc, interview = map(int,input().split())
        arr.append((doc, interview))
        
    
    arr.sort()
    
    count = 1
    interviewer = arr[0][1]
    
    for i in range(1,n):
        if arr[i][1] < interviewer:
            count += 1
            interviewer = arr[i][1]
            
    print(count)
        