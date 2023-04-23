#write a program to input a number and display all the factors of that number

num  = int(input("enter a number"))
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
print(factors)