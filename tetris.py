import time
import random

# 20행 10열
cell = [["0" for _ in range(10)] for _ in range(20)]

block_list = [1321, 14, 1212, 2212, 1222, 1311, 1331]

def output(grid):
    return '\n'.join(''.join(row) for row in grid)

def gravity(cell): # 리스트를 분석해서 중력의 영향을 받는 '1'을 한칸 아래로 떨굼
    for i in range(len(cell)-1, -1, -1):
        for j in range(len(cell[i])):
            if cell[i][j] == '1':
                cell[i][j] = '0'
                cell[i+1][j] = '1'

    return cell

making_block = 0

while True:
    cell = gravity(cell)

    if making_block == 0:
        block = str(random.choice(block_list))

        # 블록 해석: 예를 들어 block = '1321'이라면, 짝수 인덱스는 y (세로), 홀수 인덱스는 x (가로)
        for i in range(int(len(block)/2)):
            for j in range(int(block[(i+1)*2 -1])): # 아오 머리 깨지겠네
                cell[i][int(block[i*2])+j] = '1'
        making_block = 1

    print("--------------")
    print(output(cell))
    print("--------------")
    time.sleep(1)
