

import pulp


prob = pulp.LpProblem('Example2', pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')


# 
f = 3*x1 + 2*x2
prob += f


# Constraints
prob += ((2*x1 + x2) <= 6)
prob += ((7*x1 + 8*x2) <= 26)

print(prob)


optimization_result = prob.solve()
assert(optimization_result == pulp.LpStatusOptimal)

for var in (x1, x2):
    print(var.name, var.value())

import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(-10, 10)

def draw_constraint(x, fx, label):
    plt.plot(x, fx, lw=3, label=label)
    plt.fill_between(x, 0, fx, alpha=0.1)

draw_constraint(s, 6 - 2*s, 'c1')
draw_constraint(s, (26 - 7*s)/8.0, 'c2')
#draw_constraint(s, s-2, 'c3')
#draw_constraint(s, 2+s, 'c4')

plt.legend(fontsize=14)
plt.xlim(-3.0, 5.0)
plt.ylim(-3.0, 7.0)
plt.xticks(np.arange(-3, 5, 0.5))
plt.yticks(np.arange(-3, 7, 0.5))
plt.axhline(0)
plt.axvline(0)
plt.show()

