# s = {}
# for i in ['a', 'b', 'c']:
#     s[i] = input()

turn = 'a'
while True:
    if s[turn] == '':
        break
    _turn = s[turn][0]
    s[turn] = s[turn][1:]
    turn = _turn
print(turn.upper())
