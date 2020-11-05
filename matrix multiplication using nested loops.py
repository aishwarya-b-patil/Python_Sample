#matrix multiplication
M1=[[1,7,3],
    [3,5,6],
    [6,8,9]]
M2=[[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]
R=[[0,0,0,0],
   [0,0,0,0],   [0,0,0,0]]
for i in range(len(M1)):
     for j in range(len(M2[0])):
          for k in range(len(M2)):
               R[i][j]+=M1[i][k]*M2[k][j]
for r in R:
     print(r)