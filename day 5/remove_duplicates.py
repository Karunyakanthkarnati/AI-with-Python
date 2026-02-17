num = list(map(int,input('Enter Numbers :').split()))
unique = []
for i in num:
    if i not in unique:
        unique.append(i)
print(unique)
