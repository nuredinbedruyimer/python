test = int(input())


for _ in range(test):
    n, k = list(map(int, input().split()))
    
    p = len(str(k)) 
    
    arr = []
    
    for i in range(p):
        arr.append(n * 10**i)
    
    arr.reverse()
    
    i = 0  
    ans = 0 
    while i < len(arr):
        
        while k >= arr[i]:
            k -= arr[i]
            ans += 1
        i += 1
        
    print(ans+ k)
        