# 나이트가 이동할 수 있는 경우의 수
loc_data = input()
row = int(loc_data[1])
col = ord(loc_data[0]) - ord('a') + 1
mov_list = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

for mov in range(len(mov_list)):
  r = row + mov_list[mov][1]
  c = col + mov_list[mov][0]

  if r < 1 or c < 1 or r > 8 or c > 8:
    continue
  count += 1

print(count)