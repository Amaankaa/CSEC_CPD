arr = []
res = 0
for i in range(5):
  row_input = [int(x) for x in input().split()]
  arr.append(row_input)

found = False

for i in range(5):
  for j in range(5):
    if arr[i][j] == 1:
      found = True
      res += abs(3 - (i+1))
      res += abs(3 - (j+1))
      break
  if found:
    break
print (res)
  