def solution(arr, d):
    l = []

    for i in arr:
        if i % d == 0:
            l.append(i)

    if not l:
        l.append(-1)
        
    l.sort()
    
    return l
  
  # 문제: https://programmers.co.kr/learn/courses/30/lessons/12910
