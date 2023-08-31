# 7567번) 그릇

dish = input()

dish = list(dish)
height = 10
i = 1

while i < len(dish):
    if dish[i-1] == dish[i]:
        height += 5
    elif dish[i-1] != dish[i]:
        height += 10
    i += 1

print(height)