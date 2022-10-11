import numpy as np
A = np.array([[3,4,1],[9,2,3],[7,2,5]])

def gram_schmidt(A):
    Q = np.zeros(A.shape)
    R = np.zeros((A.shape[1],A.shape[1]))
    for column in range(A.shape[1]):
        #if Q is an orthonormal basis, Qt * v = Q^-1 * v (v's coordinates relative to Q basis vectors)
        linear_combo        = np.dot(a=Q.T, b=A[:,column])
        R[:     , column]   = linear_combo
        projection          = np.dot(Q, linear_combo)
        orthogonal_vector   = A[:, column] - projection
        R[column, column]   = np.dot(orthogonal_vector, orthogonal_vector)**0.5 #norm
        if R[column, column] == 0:
            raise ArithmeticError(f'The following Column is a linear combination of previous columns: {str(A[:, column])} and matrix cannot be decomposed because it is singular.')
        Q[:     , column]   = orthogonal_vector/R[column, column] #normalize
        
    return Q,R

Q,R = gram_schmidt(A)
print(Q.T@Q) # should be identity
print(Q@R) # should be A
print()
