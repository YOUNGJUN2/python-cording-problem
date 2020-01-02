def solution(s):
    answer = ''
    l = []
    
    for i in range(len(s)):
        l.append(s[i])

    l.sort(reverse=True)

    answer=''.join(l)
    
    return answer
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
