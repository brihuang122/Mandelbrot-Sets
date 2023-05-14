import numpy as np
np.random
import random

#pt 1 random n-vector
n = 5
p = np.random.rand(n)
# normalize p
p /= p.sum()

#pt 2 random nxn matrix
P = np.random.rand(n, n)
# normalize rows in P
P /= P.sum(axis=1)[:, np.newaxis]

#pt 3
N = 50
i = 1e-5
# Take steps
for k in range(N):
    p_50 = P.T.dot(p)
p_50 = p
print("p_50 =", p_50)

#pt 4
w, v = np.linalg.eig(P.T)
j_stationary = np.argmin(abs(w - 1.0))
p_stationary = v[:, j_stationary].real
p_stationary /= p_stationary.sum()
print("p_stationary = ", p_stationary)

#pt 5
temp_array = []
for i in range(n):
    temp_array.append(np.linalg.norm(p_50 - p_stationary))
print("temp_array = ", temp_array)

