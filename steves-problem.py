"""
WAP to solve the following problem.

For any given two positive integers X and Y (Y > X), find a largest positive integer K and an integer L, 
such that Y= KX + L and 0 <= L < X.


(Y - L)/X = K

"""


X = int(input())
Y = int(input())

assert Y > X   # makes sure that Y is greater than X


max = 0
for L in range(X):
    K = (Y - L)/X
    print(L, K)
    if K > max:
        max = K

print(max)
