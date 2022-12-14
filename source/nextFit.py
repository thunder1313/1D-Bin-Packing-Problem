import time

def nextFit(items, capacity):
    start = time.time()
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