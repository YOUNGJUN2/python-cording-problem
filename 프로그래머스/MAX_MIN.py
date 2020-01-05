def solution(s):
    answer = ''
    l = []
    l = s.split(" ")
    l = list(map(int, l))
    answer = "%s %s" % (min(l), max(l))
    
    return answer
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/12939
