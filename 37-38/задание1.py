list_numbers = [1, 2, 5, 3, 4, 7, 6]

count = 0
max = 0

for i in list_numbers:
    if i > max:
        max = i
    else:
        count +=1
print(count)