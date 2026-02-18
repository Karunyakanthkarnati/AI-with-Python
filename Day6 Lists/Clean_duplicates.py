nums = list(map(int,input('enter numbers: ').split()))
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
unique.sort()
print(unique)
