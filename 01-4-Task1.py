
num1,num2= map(int, input("Enter two numbers: ").split())

def prime_num(nu):
    count1=0
    for j in range(1,nu+1,1):
        if nu%j==0:
            count1+=1
    if count1==2:
        return True
def prime(num):
    c=True
    i=2
    count2=0
    while c:
        if prime_num(i)==True:
            count2+=1
        if count2==num:
            c=False
            return i
        i=i+1
res1=prime(num1)
res2=prime(num2)
print(res1,res2)

