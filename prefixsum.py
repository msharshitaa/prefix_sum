def prefix_sum(A):
    for i in range(1,len(A)):
        A[i]+=A[i-1]   
    return A
A =list(map(int, input().split()))
print(prefix_sum(A))
