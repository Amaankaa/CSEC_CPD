n = int(input())
str = str(input())

res = 0

for i in range(n - 1):
  if str[i] == str[i + 1]:
    res += 1

print (res)