def solution(n):
    sum = 0

    for i in range(1, n+1):
        if n % i == 0:
            sum += i

    return sum

  # 문제: https://programmers.co.kr/learn/courses/30/lessons/12928
