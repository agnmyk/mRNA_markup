import sys
import re
p=sys.argv[1]

fin=open(p,"r")
new=[]
line=fin.readline()
while (line!=""):
	l=re.search("> ([^ ]*.*)",line)
	if l!=None:
		line=">"+l.group(1)
	new.append(line)
	line=fin.readline()
fin.close()
out=open(p,"w")
for i in new:
	out.write(i)
out.close()
	
