# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета

# Примеры:
# 385916 -> yes
# 123456 -> no

print('Введите шестизначное число')
n = int(input())
a = n//100000
b = n//10000 % 10
c = n//1000 % 10
d = n //100 % 10
i = n //10 % 10
f = n //1 % 10

if((a+b+c) == (d+i+f)):
    print('Ваш билет счастливый')
else:
    print("Это обычный билет")