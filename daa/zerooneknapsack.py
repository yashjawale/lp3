n = 4
capacity = 5
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]

# Construct table of n+1 rows & w+1 cols
table = [[0] * (capacity + 1) for _ in range(n + 1)]

# Fill table
for i in range(1, n+1):
  for j in range(1, capacity+1):
    if (weights[i-1] <= j):
      table[i][j] = max(table[i-1][j], values[i-1] + table[i-1][j-weights[i-1]])
    else:
      table[i][j] = table[i-1][j]

print("Max possible value of sack: ", table[n][capacity])

# Backtrack to find the selected items
selected_items = []
i, j = n, capacity
while i > 0 and j > 0:
    if table[i][j] != table[i - 1][j]:
        selected_items.append(i)
        j -= weights[i-1]
    i -= 1

print("Items")
print(selected_items)