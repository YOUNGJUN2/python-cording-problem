def solution(n):
    sum = ''
    for i in range(n):
        if i % 2 == 0:
            sum += "수"
        else:
            sum += "박"
        
    return sum
  
# 문제: https://programmers.co.kr/learn/courses/30/lessons/12922
