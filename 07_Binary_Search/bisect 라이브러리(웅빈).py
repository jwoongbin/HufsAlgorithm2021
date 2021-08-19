from bisect import bisect_left, bisect_right

data = [1, 1, 2, 2, 2, 2, 3]

x = 2

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

print(count_by_range(data, x, x))
