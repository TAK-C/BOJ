N, M = map(int, input().strip().split())

A :list = []
B :list = []

# M을 입력받는 이유가 없긴 함
for i in range(N):
    temp = list(map(int, input().strip().split()))
    A.append(temp)
    
for i in range(N):
    temp = list(map(int, input().strip().split()))
    B.append(temp)
    
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=" ")
    print()