import re
import sys

f1=sys.argv[1]
f2=sys.argv[2]
f3=sys.argv[3]
f4=sys.argv[4]
if len(sys.argv)==6:
	m=sys.argv[5]
else:
	m=False

input1=open(f2, "r")

hit={}
line=input1.readline()
while re.search("^-",line)==None:
	line=input1.readline()
line=input1.readline()
#reading normal input
if not m:
	while re.search("^-",line)==None and line!="":
		h=re.search("^[^ ]+[ ]*([^ ]*)  ",line)
		if h!=None:
			if h.group(1)!="no_hit":
				hit[(re.search("(^[^ ]+) ",line).group(1))]=1
		line=input1.readline()
#reading input with chimeras
else:
	while re.search("^-",line)==None:
		chim=re.search("!Potential chimera", line)
		if chim!=None:
			hit[re.search("Query ([^ ]*)",line).group(1)]=1
		line=input1.readline()

input1.close()
input2=open(f1, "r")
out1=open(f3, "w")
out2=open(f4, "w")

line=input2.readline()
#writing fasta sequences to two files
while line!="":
	if re.search("^>",line)!=None:
		nazwa=re.search("^>[^|]*\|([^ ]*)",line)
		if nazwa!=None:	nazwa=nazwa.group(1)
		else:	nazwa=re.search("^>([^ ]*)",line).group(1)
		if nazwa in hit.keys():
			out2.write(line)
			line=input2.readline()
			while re.search("^>",line)==None and line!="":
				out2.write(line)
				line=input2.readline()
		else:
			out1.write(line)
			line=input2.readline()
			while re.search("^>",line)==None and line!="":
				out1.write(line)
				line=input2.readline()
		




