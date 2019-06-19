def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        breaker = False
        
        for j in range(2, i):
            if (i % j) == 0:
                breaker=True
                
        if breaker == True:
            continue
            
        answer = (answer+1)
        
    yield answer

print(next(solution(10)))

# 효율성 문제 해결X
# 문제: https://programmers.co.kr/learn/courses/30/lessons/12921
