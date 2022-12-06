def firstFitDecreasing(items, capacity):
    items.sort(reverse=True)
    t = 1
    binsWeights = [0]
    bins = [[]]
    for item in items:
        # loop through bins and check to which first item does fit
        for i in range(len(bins)):
            # if item fits then put it in and break the bins loop
            if (item + binsWeights[i] <= capacity):
                bins[i].append(item)
                binsWeights[i] += item
                break
            
            # at the last iteration if item was not put into any container
            # create a new container with item in it
            if (i == len(bins) - 1):
                t += 1
                binsWeights.append(item)
                bins.append([item])
                
    # display bins
    # for bin in bins:
    #     print(bin)
    return t