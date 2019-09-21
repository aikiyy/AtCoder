N, M = map(int, input().split())
diff = abs((N % 12 + M/60)/12 - M/60)
print(min(diff*360, (1-diff)*360))
