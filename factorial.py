#write a program to input a number and find the factoral of that number
num  = int(input("enter a number"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(factorial)
