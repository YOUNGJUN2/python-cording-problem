def solution(clothes):
    answer = 1
    clo_l=[]
    num_l=[]
    s=''
    
    for i in range(len(clothes)):
        clo_l.append(clothes[i][1])
        
    while len(clo_l) != 0:
        num_l.append(clo_l.count(clo_l[0]))
        s=clo_l[0]
        
        for i in range(num_l[-1]):
            clo_l.remove(s)

    for i in num_l:
        answer*=(i+1)

    return answer-1
    
    #문제: https://programmers.co.kr/learn/courses/30/lessons/42578
