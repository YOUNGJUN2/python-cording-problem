def solution(x):
    x = str(x)
    n = 0
    for i in range(len(x)):
        n+=int(x[i])

    if int(x) % n == 0:
        return True
    else:
        return False
        
#문제: https://programmers.co.kr/learn/courses/30/lessons/12947        
