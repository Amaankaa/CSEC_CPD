n = int(input())
arr = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1

    left_birds = y - 1
    right_birds = arr[x] - y

    if x > 0:
        arr[x - 1] += left_birds
    if x < n - 1:
        arr[x + 1] += right_birds

    arr[x] = 0

for birds in arr:
    print(birds)
