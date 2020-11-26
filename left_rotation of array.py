def array_rotation(array1,n,d):
    for j in range(d):
        temp=array1[0]
        for i in range(n-1):
            array1[i]=array1[i+1]
        array1[n-1]=temp
    return array1
array1=[1,2,3,4,5,6,7]
print("The array before rotation",array1)
n=len(array1)
d=int(input("enter the position by which you want to rotate"))
res=array_rotation(array1,n,d)
print("The rotated array is",res)