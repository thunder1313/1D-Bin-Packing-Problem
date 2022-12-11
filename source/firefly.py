import numpy as np
from data import item_sizes, bin_capacity
from fitness import fitness

alpha = 0.2
beta = 0.3
gamma = 0.2
num_fireflies = 5
max_iterations = 1
fireflies = [np.random.randint(0, bin_capacity, size=len(item_sizes)) for _ in range(num_fireflies)]
# print("item sizes")
# print(item_sizes)
# print("capacity")
# print(bin_capacity)
# print("initial fireflies")
# for f in fireflies:
#   print(f)

# Iterate until convergence or max iterations
while (max_iterations > 0):
  for i in range(num_fireflies-1):
    for j in range(i+1, num_fireflies):
      if fitness(fireflies[j]) > fitness(fireflies[i]):
        # Move firefly j towards firefly k
        fireflies[j] = 0.5 * fireflies[j] + 0.5 * fireflies[i]

  max_iterations -= 1

# Print the final state of the fireflies
for firefly in fireflies:
  fit = fitness(firefly)
  print(f'Fitness: {fit}')
