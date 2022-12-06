def nextFit(items, capacity):
    t = 1
    remainingSpace = [capacity]
    bins = [[]]
    
    for item in items:
        # if item fits into last opened container then put it in it
        if (remainingSpace[t-1] - item >= 0):
            remainingSpace[t-1] -= item
            bins[t-1].append(item)
        # if it does not fit then create new bin with item stored in it
        else:
            t += 1
            remainingSpace.append(capacity - item)
            bins.append([item])

    # display bins
    # for bin in bins:
    #     print(bin)
    return t