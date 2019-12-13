def solution(citations):
    answer = 0
    i = 0
    l=[]
    
    while True:
        a = b = 0
        if i > len(citations):
            break
        
        for j in citations:
            if j >= i:
                a+=1
            elif j < i:
                b+=1
        if (a>=i) and (b<=i):            
            l.append(i)
        
        i+=1

    answer=max(l)
    
    return answer
    
# https://programmers.co.kr/learn/courses/30/lessons/42747
