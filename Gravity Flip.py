n = int(input())
arr = list(map(int, input().split()))

while (True):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
      temp = arr[i] - arr[i + 1]
      arr[i + 1] += temp
      arr[i] -= temp
  
  if sorted(arr) == arr:
    break
    
print (" ".join(map(str, arr)))