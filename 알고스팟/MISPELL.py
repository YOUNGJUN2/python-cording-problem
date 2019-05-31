l = []

# 문자열을 입력받아 번호를 매겨 지울 문자의 번호를 선택해 삭제하는 기능의
# 함수를 생성한다.
def rm():
  re  = ""
  n = 1
  
  s = input()
  a=s.split()

  # 한 줄에 문자열과 해당 문자열의 삭제할 문자를 숫자로 입력받고,
  # 각각의 변수에 따로 저장한다.
  b = int(a[0])
  c = a[1]

  # 문자를 하나씩 변수에 넣어주며 삭제할 문자인지 n을 1씩 증가시켜
  # 검사하고, 삭제할 문자면 변수에 넣지않고 반복을 진행한다.
  for i in range(len(c)):
    if n == b:
      n += 1
    else:
      re += c[i]
      n += 1

  # 선택한 문자를 제외한 문자열을 리스트에 넣는다.
  l.append(re)

# 입력받을 문자열의 갯수를 입력받는다.
n = int(input())

if (1<=n<=1000):
  for i in range(n):
    rm()
    
  for i in range(n):
    print(i+1,l[i])
