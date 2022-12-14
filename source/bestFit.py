import time

def bestFit(items, capacity):
    start = time.time()
    t = 1
    remainingSpace = [capacity]
    bins = [[]]
    
    for item in items:
        bestIndex = -1
        bestRemainder = capacity + 1
        for i in range(len(bins)):
            # if item fits into bin and remaining space is the smallest yet
            # remember the index of bin
            if (remainingSpace[i] - item >= 0 and remainingSpace[i] - item < bestRemainder):
                bestIndex = i
                bestRemainder = remainingSpace[i] - item
        
        # if any bin has been selected put item in it and reduce the remaining space
        if (bestIndex != -1):
            remainingSpace[bestIndex] -= item
            bins[bestIndex].append(item)
            # reset
            bestRemainder = capacity + 1
        # if no bin has been selected (there is no bin that the item can fit into)
        # then create a new bin and place item in it
        else:
            t += 1
            remainingSpace.append(capacity - item)
            bins.append([item])
            # reser
            bestRemainder = capacity + 1
                
    end = time.time()
    # timothy = time
    timothy = end-start

    s = 0
    for space in remainingSpace:
        s += space
        
    # for bin in bins:
    #     print(bin, end=" ")
    # print()
    return t, s, timothy