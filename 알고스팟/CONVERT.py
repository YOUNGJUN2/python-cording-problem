# 계산할 값을 저장할 리스트 생성
L=[]

# 바뀔 단위를 저장할 리스트 생성
LL=[]

# kg, l, lb, g 단위들의 계산 기능의 함수 생성
def wv():
    a=""
    b=""
    c=""
    re=0
    
    l=3.7854
    lb=2.2046
    g=0.2642
    kg=0.4536

    # 값과 단위를 받아 각각의 변수에 저장한다.
    s=input()
    a=s.split()
    
    b=float(a[0])
    c=a[1]

    # 단위를 검사하여 그에 맞는 값의 계산을 한 뒤 
    # 리스트에 구해진 값과 단위를 각각 저장한다.
    if c == 'kg':
        re = b*lb
        L.append(re)
        LL.append('lb')
    elif c == 'l':
        re = b*g
        L.append(re)
        LL.append('g')
    elif c == 'lb':
        re = b*kg
        L.append(re)
        LL.append('kg')
    elif c == 'g':
        re = b*l
        L.append(re)
        LL.append('l')

n = int(input())

if 1 <= n <= 1000:
    for i in range(n):
        wv();
    for i in range(n):
        print(i+1,"%0.4f"%L[i],LL[i])
