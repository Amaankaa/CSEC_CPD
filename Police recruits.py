n = int(input())
arr = list(map(int, input().split()))

police = 0
untreatedCrime = 0

for i in range(len(arr)):
  if arr[i] < 0 and police == 0:
    untreatedCrime += 1
  elif arr[i] < 0 and police > 0:
    police -= 1
  else:
    police += arr[i]

print (untreatedCrime)