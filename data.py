
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt, floor, log10

H = 45.6
H_ = 63.5

def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))

# print("sfgs test:")
# for i in [0.0123, 12321, 34.34]:
#     print(i, round_to_1(i))

# X Values
heights = np.array([0.35, 3.70, 6.90, 8.60, 10.6, 12.9, \
    15.6, 17.3, 20.1, 23.3, 25.4, 28.4, 30.5, \
        33.3, 35.8, 37.4, 39.0]) / 100
x = (np.zeros(17) + 0.456 - heights - 0.038)

print("These are the final heights:\n", repr(x))
x_error = np.array([0.125 if i < 10 else 0.10 for i in heights])
print("And the errors:\n", repr(x_error))
x_error = np.array([0.001 if i < 10 else 0.002 for i in heights])
# print("relative uncertainty in height", x_error/x)

# Y Values
y = np.sqrt(2*9.81*(x + 0.038 + 0.635))
print("y", repr(y))
y_error = (np.zeros(17) + (x_error / x) + (0.05/63.5)) / 2 * y
print("raw y_error", repr(y_error))
y_error = np.array([round_to_1(i) for i in (np.zeros(17) + (x_error / x) + (0.05/63.5)) / 2 * y])
print("rounded y_error", repr(y_error))


# Axes labels and title
plt.title('Water Level Height v/s Jet Impact Velocity', fontsize=14)
plt.xlabel('Water Level (m)', fontsize=12)
plt.ylabel('Velocity of the plunging jet (m/s)', fontsize=12)


# plt.scatter(x, y)
plt.errorbar(x, y, yerr=y_error, fmt="o", xerr=x_error, label='Estimation of velocity from water level height', linestyle="", ecolor="black", capsize=3)


plt.legend(loc="upper left")
plt.grid(True)

plt.show()

