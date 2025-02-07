calories = list(map(int, input().split()))
black_screen = str(input())

strip_calorie = {'1': calories[0], '2': calories[1], '3': calories[2], '4': calories[3]}

res = 0

for num in black_screen:
  res += strip_calorie[num]

print (res)