N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
length = 0
left = 0
mul = 1
if 0 in S:
    length = N
else:
    for right in range(N):
        mul *= S[right]
        if mul <= K:
            length = max(length, right - left + 1)
        else:
            mul //= S[left]
            left += 1
print(length)