from data import bin_capacity
from optimalData import items, used_bins
from nextFit import nextFit
from firstFit import firstFit
from bestFit import bestFit
from firstFitDecreasing import firstFitDecreasing
from bestFitDecreasing import bestFitDecreasing

print("optimal: ", used_bins)
print("Next Fit: ", nextFit(items, bin_capacity))
print("First Fit: ", firstFit(items, bin_capacity))
print("Best Fit: ", bestFit(items, bin_capacity))
print("First Fit Decreasing: ", firstFitDecreasing(items, bin_capacity))
print("Best Fit Decreasing: ", bestFitDecreasing(items, bin_capacity))