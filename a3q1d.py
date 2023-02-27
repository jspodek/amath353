import numpy as np
import matplotlib.pyplot as plt

def my_in(a,b):
    """
    returns true if a in b, false otherwise
    """
    x = np.isclose(a,b)
    for i in x:
        if i:
            return True
    return False

def f1(x):
    return np.tan(x) 
def f2(x):
    return 2*x / (x**2 - 1)

x_vals = np.linspace(0,30,1000)

y1 = f1(x_vals)
y2 = f2(x_vals)

intersection_points = np.argwhere(np.diff(np.sign(y1 - y2))).flatten()
intersection_c_vals = np.array([x_vals[i] for i in intersection_points])

lambda_vals = []

for i in range(len(y1)):
    if my_in(y1[i], y2):
        lambda_vals.append(np.sqrt(x_vals[i]))


print(lambda_vals)

