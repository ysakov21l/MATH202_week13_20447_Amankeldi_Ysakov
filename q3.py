# MATH202 - Q3
# Student: Amankeldi Ysakov | ID: 20447
# Solve y' = x^2*y - (1/2)*y^2 with Euler's Method

import matplotlib.pyplot as plt
import datetime

# Differential equation
def f(x, y):
    return x**2 * y - 0.5 * y**2

# Euler method
def euler(f, x0, y0, h, steps):
    xs = [x0]
    ys = [y0]
    for _ in range(steps):
        y0 += h * f(x0, y0)
        x0 += h
        xs.append(x0)
        ys.append(y0)
    return xs, ys

# Initial values
x0 = 0
y0 = 1
h = 0.1
steps = int(1 / h)

# Run
x_vals, y_vals = euler(f, x0, y0, h, steps)

# Final result
print(f"Estimated y(1): {y_vals[-1]:.6f}")
print("Timestamp:", datetime.datetime.now())

# Save graph
plt.plot(x_vals, y_vals, marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler's Method for y' = x^2*y - 0.5*y^2")
plt.grid(True)
plt.savefig("q3_plot.png")
import datetime
print("Timestamp:", datetime.datetime.now())
