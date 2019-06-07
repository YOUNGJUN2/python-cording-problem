def solution(array, commands):
    answer = []

    for i in commands:
        a = array[i[0]-1:i[1]]
        b = sorted(a)
        c = b[i[2]-1]

        answer.append(c)
    return print(answer)


solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])
