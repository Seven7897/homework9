user_number = input("Введите число : ")
summ = 0
i = 0
while i < len(user_number) :
    if user_number[i] != '.':
        k = int(user_number[i])
        summ += k
        i += 1
    else :
        i+=1
print(summ)
