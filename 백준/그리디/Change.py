l = [500, 100, 50, 10, 5, 1]

n = 1000
x = int(input())

cos = n - x

re = 0

for i in l:
    if (cos // i) > 0:
        re += (cos // i)        
        cos = cos - ((cos // i) * i)
print(re)
'''

for i in l:
    while cos - i >= 0:
        cos = cos - i
        re += 1
print(re)
        
'''
        
