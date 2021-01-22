from math import ceil, sqrt

S = open('wngy-fin.min.bf').read()
l = len(S)

inner_x = 40
inner_y = 20
margin_top = 10
margin_x = 20

s = ceil(sqrt(l))
print(s)
print(s**2 - l)

n = s

for i in range(0,inner_y):
	S = S[:n*(margin_top + i) + margin_x] + ' '*inner_x + S[n*(margin_top + i) + margin_x:]


print('\n'.join([S[i:i + n] for i in range(0, len(S), n)]))