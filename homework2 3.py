user_namber = int(input("Введите число : "))
i = 1
k = 0
while i <= user_namber:
    k += (1 + 1 / i)**i
    print(f"{i} : {k}")
    i += 1