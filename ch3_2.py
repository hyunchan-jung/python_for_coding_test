N, M, K = map(int, input().split(' '))
L = list(map(int, input().split(' ')))

L.sort()     # 내림차순으로 정렬
L = L[::-1]  # 역순 정렬

answer = 0
for m in range(1, M+1):
    if m % (K+1) == 0:   # K만큼 출력했을때 두 번째로 큰 수 추가
        answer += L[1]
    else: answer += L[0] # 가장 큰 수 추가
print(answer)