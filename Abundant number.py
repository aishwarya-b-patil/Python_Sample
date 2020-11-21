def factors(num1):
    list1=[]
    for i in range(1,num1):
        if num1%i==0:       #To calculate factors and creating list
            list1.append(i)
        else:
            pass
    print(list1)
    sum=0
    for i in list1:
        sum=sum+i   #Adding all the factors of input number
    print(sum)
    if sum>num1:
        print("The number {} is an abundant number".format(num1))
    else:
        print("The number {} is not an abundant number".format(num1))
num1=int(input("enter the number"))
factors(num1)