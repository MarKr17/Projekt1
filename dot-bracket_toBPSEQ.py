# script for converting dot-bracket file to BPSEQ
opening_brackets=['(','[','{']
closing_brackets=[')',']','}']
def finding_pairs(chars):
	pairs=[]
	pair=[]
	x=0
	indexes=list(range(len(chars)))
	for i in indexes:
		if chars[i] in opening_brackets:
			pair.append(i)
			bracket=chars[i]
			bracket_index=opening_brackets.index(bracket)
			for j in range(i+1, len(chars)):
				if chars[j]==opening_brackets[bracket_index]:
					x+=1
				if chars[j]== closing_brackets[bracket_index]:
					if x==0:
						pair.append(j)
						break;
					else:
						x-=1
			pairs.append(pair)
			pair=[]
			x=0
	return pairs

def Bpseq(chars, bases):
	pairs=finding_pairs(chars)
	bpseq=[]
	line =""
	for i in (range(len(chars))):
		for pair in pairs:
			if pair[0] == i:
				x=pair[1]+1
			elif pair[1] ==i:
				x=pair[0]+1
			else:
				x=0
		line="{} {} {}".format(i+1, bases[i], x)
		bpseq.append(line)

	return bpseq

f= open("dot-brackets//1ET4-A.dbn","r")
bases=f.readline()
chars=f.readline()
f.close()
print(bases)
print()
print(chars)

print()
pairs=finding_pairs(chars)
print(pairs)

print()
bpseq=Bpseq(chars, bases)
print(bpseq)

f= open("bp_seq.txt", "w")
for line in bpseq:
	f.write(line+"\n")
f.close()