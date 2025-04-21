# MATH202 - Q1
# Student: Amankeldi Ysakov
# Student ID: 20447
# Differential Equation Comparison using Euler's Method

import matplotlib.pyplot as plt

# Euler's Method Function
def euler_method(f, x0, y0, h, steps):
    xs = [x0]
    ys = [y0]
    for _ in range(steps):
        y0 += h * f(x0, y0)
        x0 += h
        xs.append(x0)
        ys.append(y0)
    return xs, ys

# Differential Equations
def eq_A(x, y):
    return 1 + x * y

def eq_B(x, y):
    return -2 * x * y

def eq_C(x, y):
    return 1 - 2 * x * y

# Parameters
x0 = 0
y0 = 1
h = 0.1
steps = 50

# Solve with Euler's Method
x_a, y_a = euler_method(eq_A, x0, y0, h, steps)
x_b, y_b = euler_method(eq_B, x0, y0, h, steps)
x_c, y_c = euler_method(eq_C, x0, y0, h, steps)

# Plotting
plt.plot(x_a, y_a, label="A: y' = 1 + xy")
plt.plot(x_b, y_b, label="B: y' = -2xy")
plt.plot(x_c, y_c, label="C: y' = 1 - 2xy")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler's Method Comparison (Q1)")
plt.grid(True)
plt.legend()
plt.savefig("q1_plot.png")
import datetime
print("Timestamp:", datetime.datetime.now())

