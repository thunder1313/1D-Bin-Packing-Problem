import random
minWeight = 1
maxWeight = 10
numberOfItems = 10
choices = [i for i in range(minWeight, maxWeight+1)]

items = random.choices(choices, k = numberOfItems)
binCapacity = int(maxWeight*1.1) # make each bin 10% bigger than the biggest item