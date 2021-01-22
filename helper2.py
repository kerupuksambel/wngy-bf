s = 'Rinko Shirokane'
# s = open('template').read()
def is_upper(ch):
	return ord(ch) >= (64 + 1) and ord(ch) <= (64 + 26)  

def is_lower(ch):
	return ord(ch) >= (96 + 1) and ord(ch) <= (96 + 26)  

def tab(string, indent):
	if(len(string) > 0):
		print('\t' * indent + string)
		# print(string, end='')

def first_element(array):
	return array[0]

# | input |  | null | 1st loop | 2nd loop | canvas

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

# read and store input, and go back to cell after input 
tab('>+[>,]<[<]>->[>]>>', 0)
# move to 1st loop
tab('++++++++', 0)
tab('[', 0)

# canvas
## upper
tab('>++++++++', 1)
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
tab('++++++++++++', 1)
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

## symbol
if(len(sym) > 0):
	tab('++++++++', 1)
	tab('[', 1)
	counter = 0
	for u in range(len(sym)):
		if(u == 0):
			p = '>' * (sym[u][0] + 1) + '+'
			counter += (sym[u][0] + 1)
		else:
			p = '>' * (sym[u][0] - sym[u-1][0]) + '+'
			counter += (sym[u][0] - sym[u-1][0])
		tab(p, 2)
	tab('<' * counter + '-' , 2)
	tab(']', 1)

## end of canvasing
tab('[<]<-', 1)
tab(']', 0)

# 2nd phase - print mid bits
tab('++++', 0)
tab('[', 0)

## loop only for alphabet 
tab('>++++', 1)
tab('[', 1)
alphabet = lower + upper
alphabet = sorted(alphabet, key=first_element)
counter = 0
for a in range(len(alphabet)):
	div = ((ord(alphabet[a][1]) >> 2) % 8)
	if(a == 0):
		p = '>' * (alphabet[a][0] + 1) + '+' * div
		counter += (alphabet[a][0] + 1)
	else:
		p = '>' * (alphabet[a][0] - alphabet[a-1][0]) + '+' * div
		counter += (alphabet[a][0] - alphabet[a-1][0])
	tab(p, 2)
tab('<' * counter + '-' , 2)
tab(']', 1)

## end of 2nd phase
tab(']', 0)

# final phase
## loop only for alphabet
counter = 0
for a in range(len(alphabet)):
	div = ((ord(alphabet[a][1])) % 4)
	if(a == 0):
		p = '>' * (alphabet[a][0] + 1) + '+' * div
		counter += (alphabet[a][0] + 1)
	else:
		p = '>' * (alphabet[a][0] - alphabet[a-1][0]) + '+' * div
		counter += (alphabet[a][0] - alphabet[a-1][0])
	tab(p + '.', 0)
tab('<' * counter, 0)
