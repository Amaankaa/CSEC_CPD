from collections import deque
n = int(input())
arr = list(map(int, input().split()))

arr_ = deque(arr)

sereja, dima = 0, 0

turn = True

for _ in range(n):
  if turn:
    if arr_[0] > arr_[len(arr_) - 1]:
      sereja += arr_[0]
      arr_.popleft()
      turn = False
      
    else:
      sereja += arr_[len(arr_) - 1]
      arr_.pop()
      turn = False
      
  else:
    
    if arr_[0] > arr_[len(arr_) - 1]:
      dima += arr_[0]
      arr_.popleft()
      turn = True
      
    else:
      dima += arr_[len(arr_) - 1]
      arr_.pop()
      turn = True

print (sereja, dima)