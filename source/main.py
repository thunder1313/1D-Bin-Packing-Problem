from data import items, binCapacity
from nextFit import nextFit
from firstFit import firstFit

print("items: ", items)
print("bin capacity: ", binCapacity)
print("Next Fit: ", nextFit(items, binCapacity))
print("First Fit: ", firstFit(items, binCapacity))