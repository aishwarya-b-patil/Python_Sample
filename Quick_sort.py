a=[9,8,7,6,5,4,3,2,1,0]
low=0
up=len(a)-1
def partition(a,low,up):
    i=low+1
    j=up
    pivot=a[low]
    while(i<=j):
        while(a[i]<pivot and i<j):
            i+=1
        while(a[j]>pivot):
            j-=1
        if(i<j):
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        else:
            i+=1
    a[low]=a[j]
    a[j]=pivot
    return j
def quick(a,low,up):
    if(low>=up):
        return
    piv_loc=partition(a,low,up)
    quick(a,low,piv_loc-1)
    quick(a,piv_loc+1,up)
quick(a,low,up)
for i in a:
    print(i,end=" ")
