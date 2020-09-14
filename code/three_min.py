x, y, z = 3, 4, 5
small = x if x < y else y
small = small if small < z else z
print(small)