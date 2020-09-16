def alsub (*a, b=3):
    sb = 0
    for i in a:
        sb += i
    sb *= b
    return sb
print(alsub(1,1,1,1,1,1,4))

def alsub (*a, b=3):
    sb = 0
    for i in a:
        sb += i
    sb *= b
    return sb
print(alsub(1,1,1,1,1,1,4))
print(alsub(1,1,1,1,1,1,4, b=5))
