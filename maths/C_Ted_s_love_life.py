from collections import defaultdict

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    indexs_map = defaultdict(int)

    for i in range(n):
        indexs_map[arr[i]] += 1

    m = int(input())

    alpha = [0 for _ in range(26)]

    for _ in range(m):
        word = set(input())

        for char in word:
            index = ord(char) - ord("a")
            alpha[index] += 1

    index_s_map = dict(sorted(indexs_map.items(), key=lambda item: item[1], reverse=True))
    alpha.sort(reverse=True)

    is_found = False

    i = 0

    for key in index_s_map.keys():
        if index_s_map[key] != alpha[i]:
            is_found = True
            break
        i += 1

    if is_found:
        print("NO")
    else:
        print("YES")
