l=[]

# 건물의 총 전력을 입력받고 함수 안에서 9~18시 사이 시간당 전력소비량의 합과 비교해주는 함수를 생성한다.
def ai(y):
    a=input()
    b=a.split()

    # 전력이 초과되었는지 아닌지의 결과를 리스트에 인덱싱한다.
    if y >= int(b[0])+int(b[1])+int(b[2])+int(b[3])+int(b[4])+int(b[5])+int(b[6])+int(b[7])+int(b[8]):
        l.append("YES")
    else:
        l.append("NO")

    
# 건물의 갯수를 입력 받는다.
t=int(input())

# 건물의 갯수만큼 함수를 호출한다.
for i in range(t):
    y=int(input())
    ai(y)

# 함수의 결과가 저장된 리스트를 모두 출력한다.
for j in range(t):
    print(l[j])
