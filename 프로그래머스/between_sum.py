def solution(a, b):
    c = 0
    answer = 0

    if b < a:
        c = b
        b = a
        a = c
    
    if a == b:
        answer = a
    else:  
        for i in range(a, b+1):
            answer += i
        
    return answer

  # 문제: https://programmers.co.kr/learn/courses/30/lessons/12912
