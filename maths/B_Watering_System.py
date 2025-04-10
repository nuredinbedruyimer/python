n , A, B = list(map(int, input().split()))
arr = list(map(int, input().split()))

first_element = arr[0]

temp = sorted(arr[1:])[::-1]


non_blocked = sum(arr)

count = 0
is_found = False
for value in temp:
    cond = (A * first_element )/non_blocked
    if cond >= B:
        is_found = True
        
        break
    else:
        count += 1
        non_blocked -= value
        
if is_found:
    print(count)
else:
    print(n -1)
