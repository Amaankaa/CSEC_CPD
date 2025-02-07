n = int(input())
res = 0
row_poles = []

for i in range(n):
  sides = int(input())
  row_poles.append(sides)

for i in range(n-1):
  if row_poles[i] != row_poles[i + 1]:
    res += 1

res += 1
print(res)