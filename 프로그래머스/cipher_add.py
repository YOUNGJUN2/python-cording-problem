def solution(n):
    n = str(n)
    sum = 0

    for i in range(len(n)):
        sum += int(n[i])
    
    return sum

# 문제: https://programmers.co.kr/learn/courses/30/lessons/12931
