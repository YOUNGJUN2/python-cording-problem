def solution(strings, n):
    answer = []
    l = []
    for i in range(len(strings)):
        l+=[[strings[i][n], strings[i]]]
  
    l.sort()

    for i in l:
        answer.append(i[1])
    
    return answer
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
