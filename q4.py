#Initial - not for submission

def generate_bruckner(n):
    def checkvalid(A, row, col):
        for i in range(col):
            if A[row][i] == A[row][col]:
                return False
        for i in range(row):
            if A[i][col] == A[row][col]:
                return False
        return True
    
    def generate(A, index):
        if index == n * n:
            result.append([row[:] for row in A])
            return
        
        row = index // n
        col = index % n
        for num in range(1, n + 1):
            A[row][col] = num
            if checkvalid(A, row, col):
                generate(A, index + 1)
            A[row][col] = 0

    result = []
    A = [[0] * n for _ in range(n)]
    generate(A, 0)
    return result

print(generate_bruckner(3))


"""
def generate_bruckner(n):
    def checkvalid(A, row, col):
        for i in range(col):
            if A[row][i] == A[row][col]:
                return False
        for i in range(row):
            if A[i][col] == A[row][col]:
                return False
            
        return True
    
    def generate(A, index):
        if index == n * n:
            for row in A:
                result.append(row[:])
            return
        
        row = index // n
        col = index % n
        for num in range(1, n + 1):
            A[row][col] = num
            if checkvalid(A, row, col):
                generate(A, index + 1)
            A[row][col] = 0

    result = []
    #for _ in range(n):
    #    A = [[0] * n]
    A = [[0] * n for _ in range(n)]
    generate(A, 0)
    return result

print(generate_bruckner(3))

"""