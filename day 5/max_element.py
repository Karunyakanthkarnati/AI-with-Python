num = list(map(int,input('Enter numbers: ').split()))
max = num[0]
for n in num:
    if n > max :
        max = n
print('Maximum number is :',max)
