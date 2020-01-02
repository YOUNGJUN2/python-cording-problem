def solution(n):
    answer = 0
    l = []
    n = str(n)
    
    for i in range(len(n)):
        l.append(n[i])

    l.sort(reverse=True)
    answer = int(''.join(l))
    
    return answer
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/12933
