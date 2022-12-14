from data import bin_capacity
from optimalData import items, used_bins
from nextFit import nextFit
from firstFit import firstFit
from bestFit import bestFit
from firstFitDecreasing import firstFitDecreasing
from bestFitDecreasing import bestFitDecreasing

from time import time

# print("items: ", items)
print("optimal: ", used_bins)
# print("bin capacity: ", bin_capacity)
print("Next Fit: ", nextFit(items, bin_capacity))
print("First Fit: ", firstFit(items, bin_capacity))
print("Best Fit: ", bestFit(items, bin_capacity))
print("First Fit Decreasing: ", firstFitDecreasing(items, bin_capacity))
print("Best Fit Decreasing: ", bestFitDecreasing(items, bin_capacity))
# start = time()
# print(nextFit(items, bin_capacity))
# end = time()
# t1 = end - start

# start = time()
# print(firstFit(items, bin_capacity))
# end = time()
# t2 = end - start

# start = time()
# print(bestFit(items, bin_capacity))
# end = time()
# t3 = end - start

# start = time()
# print(firstFitDecreasing(items, bin_capacity))
# end = time()
# t4 = end - start

# start = time()
# print(bestFitDecreasing(items, bin_capacity))
# end = time()
# t5 = end - start

# print(t1)
# print(t2)
# print(t3)
# print(t4)
# print(t5)