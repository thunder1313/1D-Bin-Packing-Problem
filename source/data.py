import random
import json

file = open('input.json')
# returns JSON object as a dictionary
data = json.load(file)

minSize = data["min_item_size"]
maxSize = data["max_item_size"]
numberOfItems = data["number_of_items"]
bin_capacity = data["container_size"]

choices = [i for i in range(minSize, maxSize+1)]
items = random.choices(choices, k = numberOfItems)