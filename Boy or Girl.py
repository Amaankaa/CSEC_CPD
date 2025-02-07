username = str(input())
unique_characters = set(username)

if len(unique_characters) % 2 == 0:
  print ("CHAT WITH HER!")
else:
  print ("IGNORE HIM!")
  