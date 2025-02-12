s = str(input())
t = str(input())

i, j = 0, 0

while j < len(t):
  if t[j] == s[i]:
    i+=1
  j += 1

print (i + 1)