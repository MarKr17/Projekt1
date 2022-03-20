def find_single(bpseq):
	lines=[]
	begin=""
	end=""
	i=0
	while i<(len(bpseq)-1):
		strand=""
		if i==0 or bpseq[i+1][2]=="0":
			strand=strand+bpseq[i][1]
			begin=bpseq[i][0]
			j=i+1
			while j<len(bpseq) and bpseq[j][2]=="0" :
				strand= strand+bpseq[j][1]
				j=j+1
			if j>= len(bpseq):
				j=j-1
			i=j-1
			end=bpseq[j][0]
			strand=strand+bpseq[j][1]
			s="{}-{}-{}".format(begin, strand, end)
			lines.append(s)
		i=i+1
	return lines

f= open("bpseqs//1ET4-A.bpseq","r")
lines= f.readlines()

bpseq=[]
for line in lines: 
	line=line.strip()
	l=list(line.split(" "))
	bpseq.append(l)

strands= find_single(bpseq)

print(strands)

f= open("single_strands//1ET4-A.strands", "w")
for line in strands:
	f.write(line+"\n")
f.close()