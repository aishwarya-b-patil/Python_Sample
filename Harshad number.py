def sum_num1(num1):
    sum=0
    while num1>0:
        rem=num1%10   #To calculate sum of digits in the entered number
        sum=sum+rem
        num1=num1//10
    return sum
def harshad_num(num1,sum):
    res=num1%sum
    if res==0:
        print("The entered number {} is Harshad number".format(num1))
    else:
        print("The entered number {} is  not a Harshad number".format(num1))
def user():
    num1=int(input("enter the number"))
    sum=sum_num1(num1)
    harshad_num(num1,sum)
user()

