def solution(s, n):
    cryp = ''
    o = 0
    
    for i in range(len(s)):
        if ord(s[i]) == 32:
            cryp += ' '
            continue
        else:
            o = ord(s[i]) + n
            
        if (65 <= ord(s[i]) and ord(s[i]) <= 90) and 91 <= o:
            o -= 26
            cryp += chr(o)
        else:
            if 123 <= o:
                o -= 26
            cryp += chr(o)  

    return cryp
  
  # 문제: https://programmers.co.kr/learn/courses/30/lessons/12926
