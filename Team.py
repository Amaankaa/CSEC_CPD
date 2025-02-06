n = int(input())
res = 0

for _ in range(n):
  Petya, Vasya, Tonya = list(map(int, input().split()))
  sum_ = Petya + Vasya + Tonya
  if sum_ >= 2:
    res += 1

print (res)