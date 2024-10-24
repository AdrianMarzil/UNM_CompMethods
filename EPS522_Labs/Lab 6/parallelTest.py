# this code contains our test function to be run in parallel.
# we need to provide modules here that the code depends on
import numpy as np

def getFactorial(N):
    fact = np.math.factorial(N)
    return fact
