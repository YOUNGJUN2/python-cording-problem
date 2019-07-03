def solution(d, b):
    d.sort()
    n = 0
    
    for i in d:
        if i <= b:
            b -= i
            n += 1
        else:
            break
        
    return n
  
  # 문제: https://programmers.co.kr/learn/courses/30/lessons/12982
