limak, bob = list(map(int, input().split()))

years = 0

while limak <= bob:
  years += 1
  limak *= 3
  bob *= 2

print (years)