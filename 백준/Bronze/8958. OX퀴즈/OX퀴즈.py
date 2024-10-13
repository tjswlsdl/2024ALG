num = int(input())

for _ in range(num):
    question = list(input())  #_번째 question 리스트로 받고
    score = 0
    sum_score =0    
    
    for ox in question: # _번째 question OX판별후 점수매기기
        if ox == 'O': # O면 score에 +1, sum_score에 score만큼 더하기
            score +=1 
            sum_score += score
        else:
            score =0
    
    print(sum_score)