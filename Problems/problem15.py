# https://projecteuler.net/problem=15



def num_paths_lazy(n, m):
    if n == 0 and m == 0: 
        return 1
    elif n == 0:
        return num_paths_lazy(n, m-1)
    elif m == 0:
        return num_paths_lazy(n-1, m)
    else:
        return num_paths_lazy(n-1, m) + num_paths_lazy(n, m-1)
    
# print(num_paths_lazy(20, 20))

def num_paths_less_lazy(n, m):
    if n == 0 and m == 0: 
        return 0
    elif n == 0:
        return 1 
    elif m == 0:
        return 1 
    else:
        return  num_paths_less_lazy(n-1, m) + num_paths_less_lazy(n, m-1)
    
# print(num_paths_less_lazy(20,20))


def num_paths(n):
    """I assume that is nxn grid"""
    M = [[1]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i ==0 and j == 0:
                continue
            elif i == 0 and j>0: # first row
                M[i][j] = M[i][j-1]
            elif j == 0 and i>0: # first column
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = M[i][j-1] + M[i-1][j]
    return M[n][n]

print(num_paths(20))