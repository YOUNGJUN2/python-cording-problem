def solution(s):
    n = len(s)
    if n % 2 == 1:
        re = s[(n//2):((n//2)+1)]
    else:
        re = s[(n//2)-1:((n//2)+1)]
        
    return re

# 문제: https://programmers.co.kr/learn/courses/30/lessons/12903
