opening_brackets=['(','[','{']
closing_brackets=[')',']','}']
def finding_stems(chars):
	stems=[]
	stem=[]
	indexes=list(range(len(chars)))
	for i in indexes:
		if chars[i] in opening_brackets:
			stem.append(i)
			bracket=chars[i]
			indexes.remove(i)
			bracket_index=opening_brackets.index(bracket)
			for j in indexes:
				if chars[j]== closing_brackets[bracket_index]:
					stem.append(j)
					indexes.remove(j)
					break;
			stems.append(stem)
			stem=[]
	return stems
f= open("dot-brackets//1ET4-A.dbn","r")
bases=f.readline()
chars=f.readline()
f.close()

print(bases)
print()
print(chars)

print()
stems=finding_stems(chars)
print(stems)