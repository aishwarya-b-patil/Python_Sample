def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
input_list=[89,34,17,13,10,4,0]
result_list = bubble_sort(input_list)
print(result_list)