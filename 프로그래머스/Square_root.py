import math
def solution(n):
    z = math.sqrt(n)

    if z % 1 == 0:
        return int((z+1)**2)
    else:
        return -1
        
#문제: https://programmers.co.kr/learn/courses/30/lessons/12934
