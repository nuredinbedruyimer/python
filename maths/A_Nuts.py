box_section, total_nut, number_divisors, capacity_of_section = list(map(int, input().split()))

ans = 0

while total_nut > 0:
    temp = min(box_section - 1, number_divisors)
    number_divisors -= temp
    total_nut -= (temp + 1) * capacity_of_section
    ans += 1
print(ans)

    
    