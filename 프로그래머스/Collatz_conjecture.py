def solution(n):
    i = 0

    while n != 1:
        if i >= 500:
            i = -1
            break;
        
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
            
        i += 1
    return i

# 문제: https://programmers.co.kr/learn/courses/30/lessons/12943
