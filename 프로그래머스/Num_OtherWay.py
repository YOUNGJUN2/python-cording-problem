def solution(n):
    n=str(n)
    answer = []

    for i in range(len(n)-1, -1, -1):
        answer.append(int(n[i]))
    
    return answer
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/12932
