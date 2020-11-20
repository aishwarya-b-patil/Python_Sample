def num1_count(num1):
    count = 0
    while num1 > 0:
        count += 1  # To calculate the number of digits of the input number
        num1 = num1 // 10
    return count
def num1pow_sum(num1,count):
    sum = 0
    while num1 > 0:
        rem = num1% 10  #To calculate the sum of the digits of num1
        sum += rem ** count
        num1 = num1 // 10
    return sum
def user_input():
    num1=int(input("enter the number"))
    count=num1_count(num1)
    print("The number of digits present in the num1 is {}".format(count))
    sum=num1pow_sum(num1,count)
    print("The sum of digits of the num1 {}".format(sum))
    if sum==num1:
        print("The input number {} is Armstrong number".format(num1))
    else:
        print("The input number {} is not an Armstrong number".format(num1))
user_input()


