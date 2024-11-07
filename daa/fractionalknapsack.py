n = 5
capacity = 60
weights = [5, 10, 15, 22, 25]
values = [30, 40, 45, 77, 90]

# Calculate value/weight ratios
ratios = [0] * n
for i in range(n):
  ratios[i] = values[i]/weights[i]

knapsack_item_weights = [0] * n
knapsack_value = 0

sorted_item_indices = sorted(range(n), key=lambda x: ratios[x], reverse=True)

for index in sorted_item_indices:
  if capacity > 0:
    if (weights[index] <= capacity):
      # Add whole item
      knapsack_item_weights[index] = weights[index]
      capacity -= weights[index]
      knapsack_value += values[index]
    else:
      # Add fraction of item
      knapsack_item_weights[index] = capacity/weights[index]
      knapsack_value += (capacity/weights[index]) * values[index]
      capacity = 0
  else:
    break

print("Total value: ", knapsack_value)
print(knapsack_item_weights)
