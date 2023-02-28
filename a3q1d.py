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
    return np.tan(np.sqrt(x)) 
def f2(x):
    return 2*np.sqrt(x) / (x - 1)

x_vals = np.linspace(-100,100,100000)

y1 = f1(x_vals)
y2 = f2(x_vals)

plt.plot(x_vals, y1, label="tan")
plt.plot(x_vals, y2, label="rational")

plt.show()

lambda_vals = []

for i in range(len(y1)):
    if my_in(y1[i], y2):
        lambda_vals.append(x_vals[i])


print(lambda_vals)

