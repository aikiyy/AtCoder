N = int(input())-1
q, mod = divmod(N, 9)
print(str(mod+1)*(q+1))
