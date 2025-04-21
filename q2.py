# MATH202 - Q2
# Student: Amankeldi Ysakov | ID: 20447
# Alcohol mixture problem using Euler's Method

import matplotlib.pyplot as plt

# Differential equation: dA/dt = 0.275 - (5/510) * A
def dA_dt(t, A):
    return 0.275 - (5 / 510) * A

# Euler method
def euler(f, t0, A0, h, steps):
    t_values = [t0]
    A_values = [A0]
    for _ in range(steps):
        A0 += h * f(t0, A0)
        t0 += h
        t_values.append(t0)
        A_values.append(A0)
    return t_values, A_values

# Initial conditions
t0 = 0
A0 = 22.95  # 4.5% of 510 gallons
h = 0.1
steps = int(90 / h)  # simulate for 90 minutes

# Run simulation
t_vals, A_vals = euler(dA_dt, t0, A0, h, steps)

# Calculate final percentage
final_A = A_vals[-1]
final_percentage = (final_A / 510) * 100
print(f"Alcohol amount after 90 minutes: {final_A:.4f} gallons")
print(f"Alcohol percentage: {final_percentage:.4f}%")

# Plot
plt.plot(t_vals, [a / 510 * 100 for a in A_vals])
plt.xlabel("Time (minutes)")
plt.ylabel("Alcohol %")
plt.title("Alcohol Percentage Over Time (Euler’s Method)")
plt.grid(True)
plt.savefig("q2_plot.png")
import datetime
print("Timestamp:", datetime.datetime.now())
