# 그리디
N, M, K = map(int, input().split(' '))
L = list(map(int, input().split(' ')))

# 내림차순으로 정렬
L.sort()
L = L[::-1]

answer = 0
for m in range(M):
    if m > 0 and m % K == 0: # K만큼 출력했을때 다음으로 큰 수 계산
        answer += L[1]
    else: answer += L[0]
print(answer)