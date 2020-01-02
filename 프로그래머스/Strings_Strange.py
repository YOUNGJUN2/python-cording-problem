def solution(s):
    ss=''
    l = s.split(' ')

    for i in l:
        for j in range(len(i)):
            if j % 2 == 0:
                ss+=i[j].upper()
            elif j % 2 == 1:
                ss+=i[j].lower()
        ss+=' '

    ss=ss[:-1]        
            
    return ss
 
 #문제: https://programmers.co.kr/learn/courses/30/lessons/12930
