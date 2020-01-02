def solution(answers):
    answer = []
    score = [0,0,0]
    l = []
    
    aa = [1,2,3,4,5]
    bb = [2,1,2,3,2,4,2,5]
    cc = [3,3,1,1,2,2,4,4,5,5]

    aa*=2000
    bb*=1250
    cc*=1000

    aa=(aa[:len(answers)])
    bb=(bb[:len(answers)])
    cc=(cc[:len(answers)])
    
    for i in range(len(answers)):
        if aa[i] == answers[i]:
            score[0]+=1
        if bb[i] == answers[i]:
            score[1]+=1
        if cc[i] == answers[i]:
            score[2]+=1

    m = max(score)
    
    for i in range(len(score)):
        if score[i] == m:
            answer.append(i+1) 
    
    return answer
    
    #문제: https://programmers.co.kr/learn/courses/30/lessons/42840
