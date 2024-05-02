def num_within(x, start, end):
    return start <= x <= end
print("Is 3 within [2, 4]? ", num_within(3, 2, 4))
print("Is 3 within [1, 3]? ", num_within(3, 1, 3))
print("Is 10 within [2, 5]? ", num_within(10, 2, 5))