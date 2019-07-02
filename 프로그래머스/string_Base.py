def solution(s):
    try:
        if ((len(s) == 4 or len(s) == 6) and int(s) % 1 == 0):
           return True
        else:
            return False
    except:
        return False
   
# 문제: https://programmers.co.kr/learn/courses/30/lessons/12918
