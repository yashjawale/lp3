deadlines = [4, 1, 1, 1, 3]
profits = [20, 10, 40, 30, 30]

n = len(deadlines)
job_indices = sorted(range(n), key=lambda x: profits[x], reverse=True)

max_deadline = max(deadlines)

result = [-1] * max_deadline
slots = [False] * max_deadline
total_profit = 0

for job_index in job_indices:
  given_job_deadline = deadlines[job_index]
  for i in range(min(max_deadline-1, given_job_deadline-1), -1, -1):
    if not slots[i]:
      result[i] = job_index
      slots[i] = True
      total_profit += profits[job_index]
      break # Important

print("Total Profit")
print(total_profit)

print("Selected job sequence")
for r in result:
  if (r != -1):
    print(r, " ", end="")

print()