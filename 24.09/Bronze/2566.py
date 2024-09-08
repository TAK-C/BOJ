"""
문제
    9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
    이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

입력
    첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 
    주어지는 수는 100보다 작은 자연수 또는 0이다.
    
출력
    첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 
    최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.
"""

q_list :list = []

max_num :int = 0
row_max_num :int = 0
col_max_num :int = 0

max_row :int = 9
max_col :int = 9


for row in range(max_row):
    q_list.append(list(map(int, input().strip().split())))
    
for row in range(max_row):
    for col in range(max_col):
        if q_list[row][col] > max_num:
            max_num = q_list[row][col]
            row_max_num = row+1
            col_max_num = col+1
            
print(max_num)
print(row_max_num, col_max_num)
        