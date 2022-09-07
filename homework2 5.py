import random
amount = int(input("Введите количество элементов списка : "))
list = [None] * amount
list_2 = [None] * amount
for i in range(0 , amount) :
    list[i]= input(f"Заполните элемент с индексом [{i}]  : ")
print(list)
print()
for i in range(0 , len(list_2)):
    k =  random.randrange(0 , len(list_2) - i)
    list_2[i] = list[k]
    list.pop(k)
print(list_2)



# print(random.sample(list, len(list)))
