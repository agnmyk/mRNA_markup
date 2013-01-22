import re
import sys

f0=sys.argv[1]
f1=sys.argv[2]
f2=sys.argv[3]
f3=sys.argv[4]
f4=sys.argv[5]
f5=sys.argv[6]
f6=sys.argv[7]
f7=sys.argv[8]
f8=sys.argv[9]
f9=sys.argv[10]
f10=sys.argv[11]
o=sys.argv[12]
licz=0
licz_list=[]
out=open(o, "w")
for i in xrange(1,12):
	tmp=open(sys.argv[i], "r")
	line=tmp.readline()
	while line!="":
		if re.search("^>",line)!=None:
			licz+=1
		line=tmp.readline()

	print licz
	licz_list.append(licz)
	licz=0
	tmp.close()
out.write("mRNAmarkup Report\n\n\nNumber of input sequences:\t%d\nNumber of potential vector-contaminated sequences:\t%d\nNumber of potential bacterial-contaminated sequences:\t%d\nNumber of sequences matching the ReferenceDB:\t%d\nNumber of potential full-length coding sequences:\t%d\nNon-qualifying sequences:\t%d\nNumber of potential chimeric sequences:\t%d\nNon-qualifying sequences:\t%d\nNumber of sequences matching the AllProteinDB:\t%d\nNumber of sequences matching the ProteinDomainDB:\t%d\nNumber of remaining sequences:\t%d\n" %(licz_list[0], licz_list[1],licz_list[2], licz_list[3],licz_list[4], licz_list[5],licz_list[6], licz_list[7],licz_list[8], licz_list[9], licz_list[10]))
out.close()
