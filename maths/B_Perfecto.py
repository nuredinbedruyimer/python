test = int(input())

for _ in range(test):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        arr = [i for i in range(1, n + 1)]
        arr[1], arr[0] = arr[0], arr[1]
        
        print(*arr)