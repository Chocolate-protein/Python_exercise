# 2941번) 크로아티아 알파벳

string = str(input())
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for c in cro:
    for _ in range(0, len(string)):
        if c in string:
            string = string.replace("{}".format(c), "_")

print(len(string))