def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
def MATRIX_PATH(i,j):
    if(i==0 and j == 0):
        return matrix[0][0]
    if i==0:
        return matrix[i][j]+MATRIX_PATH(i,j-1)
    if j==0:
        return matrix[i][j]+MATRIX_PATH(i-1,j)
    else:
        return matrix[i][j]+max(MATRIX_PATH(i-1,j),MATRIX_PATH(i,j-1))
    
arr=[0,0,0,0,0]
for a in range(len(arr)):
    arr[a]=Fibonacci(a+1)
print(arr)

matrix=[[6,7,12,5],[5,3,11,18],[7,17,3,3],[8,10,14,9]]
print(MATRIX_PATH(3,3))
