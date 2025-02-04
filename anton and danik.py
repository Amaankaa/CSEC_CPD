n = int(input())

games = str(input())

anton_count = 0
danik_count = 0

for char in games:
  if char == 'A':
    anton_count += 1
  else:
    danik_count += 1

if anton_count > danik_count:
  print ("Anton")
elif danik_count > anton_count:
  print ("Danik")
else:
  print ("Friendship")