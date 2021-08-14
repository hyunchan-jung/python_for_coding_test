# 행, 열 크기 지정 및 행렬 데이터 입력받기
N, M = map(int, input().split(' '))
L = []
for _ in range(N):
    L.append(list(map(int, input().split(' '))))

L.sort(key=lambda x: min(x)) # 리스트 내 각요소의 최소값 기준으로 정렬
print(min(L[-1]))  # 마지막요소(최소값이 가장 큰)의 최소값 출력