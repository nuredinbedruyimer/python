n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

pos = [0 for _ in range(n + 1)]

for i in range(n):
    pos[arr[i]] = i

#  mark the foe interval(pait)

dp = [0 for _ in  range(n)]



for _ in range(k):
    a, b = map(int, input().split())
    pos_a = pos[a]
    pos_b = pos[b]
    if pos_a > pos_b:
        dp[pos_a] = max(pos_b + 1, dp[pos_a])
    else:
        dp[pos_b] = max(pos_a + 1, dp[pos_b])

left = 0
ans = 0

for right in range(n):
    left = max(dp[right], left)
    
    ans += right - left + 1

print(ans)

        
        
    