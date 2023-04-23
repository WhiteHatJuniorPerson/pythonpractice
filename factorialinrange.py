#1!+2!+3!+4!.......n!
n = int(input("enter a number"))
sum=0
for i in range(1,n+1):
    factorial=1
    for j in range(1,i+1):
        factorial=factorial*j
    sum+=factorial
print(sum)
