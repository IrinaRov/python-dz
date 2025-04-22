list_number = [6]
count = 0
number = 0



for i in range(len(list_number)):
    if i % 2 == 0:
        count += list_number[i]

if list_number == []:
    number = 0
else:
    number = count*list_number[-1]
print(number)