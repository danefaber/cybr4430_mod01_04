#  function that takes two equal dimensioned complex vectors/matrices as its inputs and returns a vector/matrix that is obtained by adding its two inputs.
def matAdd(m1,m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] 
            for i in range(len(m1))]
    
    
#  function that takes a scalar and a complex vector/matrix as its two inputs and returns a vector/matrix that is a product of its two inputs.
def scalarMatMult(s,m1):
    return [[s * m1[i][j] for j in range(len(m1[0]))] 
            for i in range(len(m1))]
    
# function that takes a well-formed matrix/vector as its input and returns the transpose of its input.
def transpose(m1):
    return [[m1[j][i] for j in range(len(m1))] 
            for i in range(len(m1[0]))]

# function that takes a well formed matrix/vector as its input and returns the conjugate of its input.
def conjugate(m1):
    return [[m1[i][j].conjugate() for j in range(len(m1[0]))] 
            for i in range(len(m1))]

# function that applies the dagger operation on a matrix/vector and returns the result.
def conjugTranspose(m1):
    return transpose(conjugate(m1))
