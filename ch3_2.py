# �׸���
N, M, K = map(int, input().split(' '))
L = list(map(int, input().split(' ')))

# ������������ ����
L.sort()
L = L[::-1]

answer = 0
for m in range(M):
    if m > 0 and m % K == 0: # K��ŭ ��������� �������� ū �� ���
        answer += L[1]
    else: answer += L[0]
print(answer)