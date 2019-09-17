xa, ya, xb, yb, xc, yc = map(int, input().split())
a = ((xb-xa)**2 + (yb-ya)**2)**0.5
b = ((xc-xb)**2 + (yc-yb)**2)**0.5
c = ((xa-xc)**2 + (ya-yc)**2)**0.5
s = (a + b + c) / 2
print((s*(s-a)*(s-b)*(s-c))**0.5)
