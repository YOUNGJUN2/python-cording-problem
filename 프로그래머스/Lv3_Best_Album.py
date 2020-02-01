def solution(genres, plays):
    answer = []
    l = [0]*len(genres)
    ll = []
    result = 0
    re = []
    q = []
    s = ''

    for i in range(len(genres)):
        l[i] = [plays[i],genres[i],i]

    while len(l) != 0:
        s = l[0][1]
        for i in range(len(l)):
         
            if s == l[i][1]:
                ll.append(l[i])
                
        ll.sort(reverse=True)       
        answer.append(ll)

        for j in ll:
            l.remove(j)

        for i in range(len(ll)):
            result += ll[i][0]

        re.append(result)
        
        result = 0
        ll=[]    
    print(re)
    while len(answer) != 0:
        if len(answer[re.index(max(re))]) == 1:
            q.append(answer[re.index(max(re))][0][2])
        elif (answer[re.index(max(re))][0][0]) == (answer[re.index(max(re))][1][0]):
            if answer[re.index(max(re))][0][2] > answer[re.index(max(re))][1][2]:
                q.append(answer[re.index(max(re))][1][2])
                q.append(answer[re.index(max(re))][0][2])
        else:
            q.append(answer[re.index(max(re))][0][2])
            q.append(answer[re.index(max(re))][1][2])
        
        answer.remove(answer[re.index(max(re))])
        re.remove(max(re))
    
    return q
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/42579
