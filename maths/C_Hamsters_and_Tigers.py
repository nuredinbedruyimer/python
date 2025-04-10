def min_cost(word):
    #  count number of T or H
    
    window = 0
    
    for char in word:
        if char == "T":
            window += 1
            
    ans = float("inf")
    count = 0
    
    for i in range(window):
        if word[i] == "H":
            count += 1
    ans = min(ans, count)
    for i in range(window, len(word)):
        
        if word[i] == "H":
            count += 1
        if word[i - window] == "H":
            count -= 1
        
        ans = min(ans, count)
    return ans


n = int(input())
word = list(input())

ans = float("inf")

for i in range(n):
    new_word = word[i : n] + word[0: i]
    ans = min(ans, min_cost(new_word))
print(ans)
    
    


        
            