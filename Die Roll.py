import math

Y, W = map(int, input().split())

Max = max(Y, W)
numerator = 6 - Max + 1
denominator = 6

gcd_value = math.gcd(numerator, denominator)
numerator //= gcd_value
denominator //= gcd_value

print(str(numerator) + "/" + str(denominator))
