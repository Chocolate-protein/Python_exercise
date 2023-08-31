# 10886번) 0 = not cute / 1 = cute

n = int(input())
cute = 0

for _ in range(n):
    research = int(input())
    if research == 1:
        cute += 1
    else:
        cute -= 1

if cute > 0:
    print("Junhee is cute!")
elif cute < 0:
    print("Junhee is not cute!")
