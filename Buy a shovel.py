k, r = map(int, input().split())
i = 1

while (True):
  total = k * i
  change = total - r
  if total % 10 == 0:
    break
  elif change % 10 == 0:
    break
  i += 1

print (i)
  