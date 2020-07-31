A=[[1,2],[3,4]]
B=[[10,20],[30,40]]
result=[[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
for i in result:
    print(i)