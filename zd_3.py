#3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import os
os.system('cls||clear')
def summa(num):
    return sum(map(int, num.replace('.', '').replace('-', '')))
num = input('Ведите число: ')
print(f'Сумма цифр в числе: {summa(num)}')