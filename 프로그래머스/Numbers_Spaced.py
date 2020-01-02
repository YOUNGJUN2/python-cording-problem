def solution(x, n):
    answer = []

    if x > 0:
        for i in range(x, (x*n)+1, x):
            answer.append(i)
    elif x < 0:
        for i in range(x, (x*n)-1, x):
            answer.append(i)
    elif x == 0:
        for i in range(n):
            answer.append(0)
            
    return answer

#문제: https://programmers.co.kr/learn/courses/30/lessons/12954
