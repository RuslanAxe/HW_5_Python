# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
n = int(input("Введите число: "))
power = int(input("Введите степень числа: "))
def degree (n, power):
    if power == 0:
        return 1
    return n * degree(n, power - 1)
print (degree(n, power))