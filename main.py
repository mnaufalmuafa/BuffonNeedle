import random
import math

d = 5
l = 3
i = 1
Q = 0
N = 10000

x = []
theta = []

def mutlak(c) :
    return c if c >= 0 else -c

while i <= N :
    x.append(random.uniform(0,d))
    theta.append(random.randint(0,360))
    i = i + 1

i = 0

for xi in x :
    if xi < l*mutlak(math.cos(theta[i])) :
        Q = Q + 1
    i = i + 1

pi = (2*l/d)*(N/Q)

print(pi)