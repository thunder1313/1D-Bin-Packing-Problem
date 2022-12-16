import random
# import essential data from data.py
from data import choices, numberOfItems, bin_capacity

# initialize containers, number of used bins and list of items
bins = [bin_capacity]
used_bins = 1
items = []

# loop to insert each item into a bin
for i in range(numberOfItems):
    # choose random size of item
    item = random.choice(choices)
    # if item fits into a bin put it in and append item to items list
    if (bins[used_bins - 1] - item) >= 0:
        bins[used_bins-1] -= item
        items.append(item)
        # if item was put into bin and it took the whole available space open new bin
        if (bins[used_bins-1] == 0):
            used_bins += 1
            bins.append(bin_capacity)
    # if item does not fit into bin make it smaller so it does   
    else:
        item = bins[used_bins-1]
        items.append(item)
        bins[used_bins-1] -= item
        # if it wasn't the last item open new bin
        if (i != numberOfItems):
            used_bins += 1
            bins.append(bin_capacity)
# if the last bin is not fully filled fill it up with additional item
if (bins[-1] != 0):
    items.append(bins[-1])
    bins[-1] = 0
    numberOfItems += 1
# randomize the order of items
random.shuffle(items)