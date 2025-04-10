test = int(input())


for _ in range(test):
    n = int(input())
    
    
    arr = len(set(list(map(int, input().split()))))
    brr = len(set(list(map(int, input().split()))))
    
    if arr * brr >= 3:
        print("YES")
    else:
        print("NO")
    