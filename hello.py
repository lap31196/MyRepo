import numpy as np

R= np.array([[0.5,0.5,0,0],
             [-0.5,0.5,0,0],
             [0,0,1,0],
             [0,0,0,1]])
R_inv = np.linalg.inv(R)
C = np.array([1,0,0,0])
print (R)
print (R_inv)
print (np.matmul(C,R))
print (C@R)

