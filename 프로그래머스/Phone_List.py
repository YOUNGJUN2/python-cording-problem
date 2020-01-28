def solution(phone_book):
    phone = sorted(phone_book)

    for a, b in zip(phone, phone[1:]):
        if b.startswith(a):
            return False
    return True
    
#문제: https://programmers.co.kr/learn/courses/30/lessons/42577
