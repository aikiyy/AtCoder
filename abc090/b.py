def isPalindrome(s5):
    if s5[0] == s5[-1] and s5[1] == s5[-2]:
        return True
    return False


a, b = map(int, input().split(' '))
ans = 0
for i in range(a, b+1):
    if isPalindrome(str(i)):
        ans += 1
print(ans)