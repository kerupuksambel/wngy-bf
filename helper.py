# s = open('template').read()
s = 'Rinko-chan!'
def is_upper(ch):
	return ord(ch) >= (64 + 1) and ord(ch) <= (64 + 26)  

def is_lower(ch):
	return ord(ch) >= (96 + 1) and ord(ch) <= (96 + 26)  

def tab(string, indent):
	if(len(string) > 0):
		print('\t' * indent + string)
# prep
## convention
## [[index, value], ...]
upper = []
lower = [] 
sym = []
for i in range(len(s)):
	if is_upper(s[i]):
		upper.append([i, s[i]])
	elif is_lower(s[i]):
		lower.append([i, s[i]])
	else:
		sym.append([i, s[i]])
# create environment (first 3 bit)
tab('>' * len(sym), 0)
tab('++++++++', 0)
tab('[', 0)

## upper
tab('>++++++++++++', 1)
tab('[', 1)
counter = 0
for u in range(len(upper)):
	if(u == 0):
		p = '>' * (upper[u][0] + 1) + '+'
		counter += (upper[u][0] + 1)
	else:
		p = '>' * (upper[u][0] - upper[u-1][0]) + '+'
		counter += (upper[u][0] - upper[u-1][0])
	tab(p, 2)
tab('<' * counter + '-' , 2)
tab(']', 1)


## lower
tab('++++++++', 1)
tab('[', 1)
counter = 0
for u in range(len(lower)):
	if(u == 0):
		p = '>' * (lower[u][0] + 1) + '+'
		counter += (lower[u][0] + 1)
	else:
		p = '>' * (lower[u][0] - lower[u-1][0]) + '+'
		counter += (lower[u][0] - lower[u-1][0])
	tab(p, 2)
tab('<' * counter + '-' , 2)
tab(']', 1)

tab('[<]<-', 1)
tab(']', 0)

## symbol (general algorithm)
tab('<' * len(sym), 0)

# middle 3 bit
# manual last 3 bit and print 