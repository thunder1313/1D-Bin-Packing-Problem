import random
from data import choices, numberOfItems, bin_capacity

bins = [bin_capacity]
used_bins = 1
items = []

for i in range(numberOfItems):
    item = random.choice(choices)
    if (bins[used_bins - 1] - item) >= 0:
        bins[used_bins-1] -= item
        items.append(item)
        if (bins[used_bins-1] == 0):
            used_bins += 1
            bins.append(bin_capacity)    
    else:
        item = bins[used_bins-1]
        items.append(item)
        bins[used_bins-1] -= item
        if (i != numberOfItems):
            used_bins += 1
            bins.append(bin_capacity)
if (bins[-1] != 0):
    items.append(bins[-1])
    bins[-1] = 0
    numberOfItems += 1
random.shuffle(items)