l=[]

# 문자열을 입력받아 암호화시키는 함수 생성.
def md():
    s=input()
    a=""
    b=""

    # 각 문자에 번호를 매겨 짝수자리 문자만 저장한다.
    for i in range(0,len(s),2):
        a=a+s[i]
        
    # 각 문자에 번호를 매겨 홀수자리 문자만 저장한다.    
    for i in range(1,len(s),2):
        b=b+s[i]

    # 짝수자리 문자 + 홀수자리 문자의 조합으로 합쳐 암호화 시킨뒤 리스트에 인덱싱한다.
    l.append(a+b)

# 암호화 시킬 문자열의 갯수를 받는다. 조건 [ 1이상 10이하 ]
t=int(input())

if 1<=t<=10:
    for i in range(t):
        md()

    for i in range(t):
        print(l[i])
