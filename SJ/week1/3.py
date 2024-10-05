def solution(mats, park):
    answer = 0

    ## 내림 차순 정렬
    mats.sort(reverse=True)
    
    for m in mats:  ## 돗자리 크기
        check = False
        for i in range(0, len(park)-m+1):
            for j in range(0, len(park[i])-m+1):

                ## 돗자리 검사
                for k in range(i, i+m):
                    for c in range(j, j+m):
                        if park[k][c] == "-1":
                            check = True
                        else:
                            check = False
                            break
                    
                    ## 탈출
                    if check == False:
                        break
                    
                if check == True:
                    answer = m
                    return answer
                
    answer = "-1"
    return answer

mats = [1, 2]
park = [["A", "-1"], 
        ["A", "-1"]]

print(solution(mats, park))

