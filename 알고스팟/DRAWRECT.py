l = []
n = 0

# 직사각형을 이루는 네 개의 꼭지점 중 세 좌표가 주어졌을 떄 나머지 한 개의 점 좌표를
# 구하는 함수를 생성
def ai():
  a = input()
  b = input()
  c = input()

  a=a.split()
  b=b.split()
  c=c.split()

  # 나머지 한 개의 점 좌표를 리스트에 인덱싱
  if a[0]==b[0]:
    l.append(c[0])
  elif b[0]==c[0]:
    l.append(a[0])
  else:
    l.append(b[0])

  if a[1]==b[1]:
    l.append(c[1])
  elif b[1]==c[1]:
    l.append(a[1])
  else:
    l.append(b[1])

# 사용자로부터 직사각형 갯수를 입력받음
t = int(input())

# 입력받은 사각형의 갯수 만큼 함수를 실행
for i in range(t):
  ai()

# 함수에서 계산된 좌표들을 한 줄에 x, y좌표 각각 하나씩 출력
for j in range(t*2):
  print(l[j], end=" ")
  n+=1
  if (n%2 == 0):
    print("")
