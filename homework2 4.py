import random
from turtle import position
user_number = int(input("Введите число : "))
list = []
for i in range(0 , user_number):
    list.append(random.randint(-user_number,user_number))
print(list)
position_1 = int(input("Введите первую позицию элемента : "))
position_2 = int(input("Введите вторую позицию элемента : "))
print(f"Произведение будет равно : ({list[position_1] * list[position_2]})")
