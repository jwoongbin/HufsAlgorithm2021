position = input()  # 시작 위치
row = int(position[1])  # 행
column = int(ord(position[0])) - int(ord('a')) + 1  # 열(숫자로 치환)

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
