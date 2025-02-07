start = "a"
res = 0

name = str(input())

for char in name:
  clockwise = (ord(char) - ord(start) + 26)%26
  counterClockwise = 26 - clockwise
  temp = min(clockwise, counterClockwise)
  start = char
  res += temp

print (res)