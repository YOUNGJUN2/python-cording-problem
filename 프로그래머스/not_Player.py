import collections

def solution(participant, completion):
    answer = ''

    l = list(set(participant) - set(completion))    
    
    if not l:
        a = collections.Counter(participant)
        b = collections.Counter(completion)
        
        c = a-b
        c = list(c.keys())
        
        answer = c.pop()   
        
    else:
        answer = l.pop()
        
    return answer

# 문제: https://programmers.co.kr/learn/courses/30/lessons/42576
