def solution(phone_number):
    s = ''
    for i in range(len(phone_number)-4):
        s+="*"
    s += phone_number[-4:]
    return s
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/12948   
