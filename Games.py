n = int(input())
arr = []

res = 0

for _ in range(n):
  home, guest = list(map(int, input().split()))
  arr.append([home, guest])

for i in range(n - 1):
  for j in range(i+1, n):
    if arr[i][0] == arr[j][1]:
      res += 1
    if arr[i][1] == arr[j][0]:
      res += 1

print (res)
