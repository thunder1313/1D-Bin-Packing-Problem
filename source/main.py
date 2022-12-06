from data import items, binCapacity
from nextFit import nextFit
from firstFit import firstFit
from bestFit import bestFit
from firstFitDecreasing import firstFitDecreasing
from bestFitDecreasing import bestFitDecreasing

from time import time

print("items: ", items)
print("bin capacity: ", binCapacity)
print("Next Fit: ", nextFit(items, binCapacity))
print("First Fit: ", firstFit(items, binCapacity))
print("Best Fit: ", bestFit(items, binCapacity))
print("First Fit Decreasing: ", firstFitDecreasing(items, binCapacity))
print("Best Fit Decreasing: ", bestFitDecreasing(items, binCapacity))
# start = time()
# print(nextFit(items, binCapacity))
# end = time()
# t1 = end - start

# start = time()
# print(firstFit(items, binCapacity))
# end = time()
# t2 = end - start

# start = time()
# print(bestFit(items, binCapacity))
# end = time()
# t3 = end - start

# start = time()
# print(firstFitDecreasing(items, binCapacity))
# end = time()
# t4 = end - start

# start = time()
# print(bestFitDecreasing(items, binCapacity))
# end = time()
# t5 = end - start

# print(t1)
# print(t2)
# print(t3)
# print(t4)
# print(t5)