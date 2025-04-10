def _lps(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0  
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    
    return lps

def search(text, pattern):
    n, m = len(text), len(pattern)
    lps = _lps(pattern)
    j = 0  
    result = []
    
    for i in range(n): 
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == m:  # Found pattern
            result.append([i - m + 1, i])  # Store [start, end] of match
            j = lps[j - 1]
    
    return result

# Input
direction = input().strip()
n = int(input().strip())

all_words = []
for _ in range(n):
    word = input().strip()
    all_words.append(word)
right_end = len(direction)
length = 0
pos = 0
for i in range(len(direction) - 1, -1, -1):
    for word in all_words:
        if direction[i : i + len(word)] == word:
            right_end = min(right_end, i + len(word) - 1)
    if right_end -  i > length:
        length = right_end - i
        pos = i
print(length, pos)
    
