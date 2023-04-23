#write a program to input a number and check whether it is prime or not
num = int(input("enter a number"))
factors = 0
for i in range(1,num+1):
    if num%i==0:
        factors+=1
if factors==2:
    print("the number is prime")
else:
    print("number is not prime")


