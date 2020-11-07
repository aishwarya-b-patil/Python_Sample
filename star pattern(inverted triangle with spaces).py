def pattern(r,c):
    for i in range(1,r+1):
        k=1
        for j in range(1,c+1):
            if(j>=i and j<=c+1-i and k):
                print("*",end=" ")
                k=0
            else:
                print(" ",end=" ")
                k=1
        print()
row=int(input("enter the row number"))
col=int(input("enter the column number"))
pattern(row,col)

