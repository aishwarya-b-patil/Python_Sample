M1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
M2=[[9,8,7],
    [6,5,4],
    [3,2,1]]
ADD=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(M1)):
    for j in range(len(M1[0])):
        ADD[i][j]=M1[i][j]+M2[i][j]
for i in ADD:
    print(i)