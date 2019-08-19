n = int(input())
a = list(map(int, input().split()))

ans = 0
left = 0
right = 0

while left <= n-1:
    right = max(left, right)
    while right <= n-1:
        if left == right or a[right-1] < a[right]:
            right += 1
        else:
            break
    ans += right - left
    left += 1
print(ans)
