def solution(arr):
    arr.remove(min(arr))

    if len(arr) == 0:
        return -1
    else:
        return arr
        
#문제: https://programmers.co.kr/learn/courses/30/lessons/12935       
