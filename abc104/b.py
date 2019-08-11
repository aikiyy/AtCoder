import string


s = input()
if s[0] == 'A' and s[2:-1].count('C') == 1 \
    and len(set(s.replace('A', '').replace('C', '')) & set(string.ascii_uppercase)) == 0:
    print('AC')
else:
    print('WA')
