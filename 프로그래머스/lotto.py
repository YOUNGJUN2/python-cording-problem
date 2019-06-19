import random

def lotto_game(n):
    ln = []
    
    for i in range(n):
        lr=[]
        
        while len(lr)!=6:
            a = random.randint(1,45)
            breaker = False
            
            for k in lr:
                if k == a:
                    breaker = True
                    
            if breaker == True:
                continue
                
            lr.append(a)
            
        lr.sort()
        ln.append(lr)
        
        print(ln[i])
        
n = int(input("게임 수를 입력하세요: "))
lotto_game(n)
