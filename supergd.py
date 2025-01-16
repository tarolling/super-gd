import math

# define any k-lipschitz function
def f(x):
  return x * math.sin(x)

def F(x):
  return (f(x) - f(y)) / (x - y)

# hyperparams
a = 0
b = 50
tolerance = 0.01
step = 0.001

# descent loop
num_updates = 0
x1_n = a
x2_n = b

while abs(x_2n - x_1n) * (1 + abs(F(x_2n, x_1n))) > tolerance:
    if f(x_2n) - f(x_1n) < 0:
        x_1n += -step * (x_1n - x_2n) * (1 - F(x_2n, x_1n))
        updates += 1
    else:
        x_2n += -step * (x_2n - x_1n) * (1 + F(x_2n, x_1n))
        updates += 1

print(f"GLOBAL MINIMUM: {x_1n}, {f(x_1n)}")
print("TOTAL UPDATES:", updates)
