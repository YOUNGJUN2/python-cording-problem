from collections import Counter

def solution(participant, completion):
    answer = ''

    a = Counter(participant)
    b = Counter(completion)

    answer = a - b
    answer = list(answer.keys())
    answer = answer.pop()
    
    return answer

# 문제: https://programmers.co.kr/learn/courses/30/lessons/42576
