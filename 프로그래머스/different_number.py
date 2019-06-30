def solution(arr):
    
    answer = []
    x = 10
    
    for n in arr:
        if x == n:
            continue
        answer.append(n)
        x = n
        
    return answer

# 문제: https://programmers.co.kr/learn/courses/30/lessons/12906
