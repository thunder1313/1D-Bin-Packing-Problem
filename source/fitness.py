from data import item_sizes, bin_capacity

def fitness(state):
  used_bins = 0
  bin_contents = [[] for _ in range(len(state))]
  for item in item_sizes:
    found_bin = False
    for j, used_space in enumerate(state):
      print("---")
      print(j, used_space)
      print(state)
      if used_space + item <= bin_capacity:
        bin_contents[j].append(item)
        state[j] += item
        found_bin = True
        break
    if not found_bin:
      used_bins += 1
      bin_contents[used_bins - 1].append(item)
      state[used_bins - 1] += item
      
  print("bin contents from fitness")
  print(bin_contents)
  return used_bins