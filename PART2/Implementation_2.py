position = input()

position_row = int(position[1])
position_column = int(ord(position[0])) - int(ord('a')) + 1

direction = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

cnt = 0

for step in direction:
    nx = position_row + step[0]
    ny = position_column + step[1]

    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        cnt += 1

print(cnt)

