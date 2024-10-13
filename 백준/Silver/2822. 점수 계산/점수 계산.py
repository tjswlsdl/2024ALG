scores = []
for i in range(8):
    score = int(input())
    scores.append((score, i+1))  # 점수와 문제 번호를 튜플로 저장

sorted_scores = sorted(scores, key=lambda x: -x[0])  # 점수를 기준으로 내림차순 정렬
top5 = sorted_scores[:5]  # 상위 5개 선택

total_score = sum(score for score, idx in top5)
print(total_score)

problem_numbers = sorted(idx for score, idx in top5)
print(*problem_numbers)