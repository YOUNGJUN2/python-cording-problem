def solution(progresses, speeds):
    answer = []
    l=[0]
    n = 0
    
    for a, b in zip(progresses, speeds):
        while a < 100:
            a+=b
            n+=1
        if l[-1] > n:
            l.append(l[-1])
        else:
            l.append(n)
        n=0
        
    l = l[1:]

    while len(l) != 0:
        answer.append(l.count(l[0]))
    
        for i in range(answer[-1]):
            l.remove(l[0])

    return answer
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/42586
