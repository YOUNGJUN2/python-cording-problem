def solution(heights):
    answer = heights.copy()
    answer = [0 for i in answer]

    for i in range(len(heights)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if heights[j] > heights[i]:
                del answer[i]
                answer.insert(i,j+1)
                break

    return answer
    
    # 문제: https://programmers.co.kr/learn/courses/30/lessons/42588
