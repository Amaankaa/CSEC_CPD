str1 = str(input())
str2 = str(input())

str1_ = str1.lower()
str2_ = str2.lower()

res = 0

for i in range(len(str1)):
  if str1_[i] > str2_[i]:
    res = 1
    break
  elif str1_[i] < str2_[i]:
    res = -1
    break

print (res)


