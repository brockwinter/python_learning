
def pow(x, y):
    global z
    if y == 1:
        return x
    else:
        return x*pow(x, y-1)
print(pow(2, 3))