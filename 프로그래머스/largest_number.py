def solution(numbers):
    answer = ''
    l=[]
    
    for i in numbers:
        a=str(i)
        if len(a)==4:
            b=a*4
            b=b[0:4]
        if len(a)==3:
            b=a*4
            b=b[0:4]
        if len(a)==2:
            b=a*4
            b=b[0:4]
        if len(a)==1:
            b=a*4
        
        l.append([b,a])
    
    l.sort(reverse=True)
    
    for i in l:
        answer+=i[1]

    if sum(numbers)==0:
        answer='0'
        
    return answer
 
# https://programmers.co.kr/learn/courses/30/lessons/42746
