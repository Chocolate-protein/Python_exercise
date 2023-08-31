# 5717번) 상근이의 친구들

while True:
    male, female = map(int, input().split())
    if male == 0 and female == 0:
        break
    print(male + female)