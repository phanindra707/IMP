# note this code gives the outputs where functions are declared in ccextractor.c file with some specific data structures
f = open('ccextractor.c','r')

read_data = f.read()
#print read_data
rea = read_data.split('\n') # splitting file into lines 
#h = [] #for all thre lines beggining with headers
#le = 0
#em = []
#print len(rea)
#rea.remove("")
#print len(rea)
#print rea[1][0]
#for i in rea:
#	if i[0] == "#":
#		print i	
	
	


#j = 0
#for i in rea:
	#if i[0] == "#":
	#	h.append(j)
	#j = j + 1
#	print i

#for  i in h:
#	print rea[i]

#for i in rea:
#	print i
test = ['void','int','boolean','struct','char'] #took some example data types where most will be like these
l = []       # an array which stores all the lines with "(" present
st = 0       # length of list l
for i in rea:
	for z in range(0,len(i)):
		if i[z] == "(":
			l.append(st)
	st = st + 1

sc1 = [] # has the lines with "("
ans = [] # the sub sub array of sc1 where space is present and we will split it
for i in l:
	#print rea[i]
	sc1.append(rea[i].split("("))
	#print sc1[0]
	#print sc1[0][0]

	for j in range(0,len(sc1[0][0])):
		if sc1[0][0][j] == " ":
			ans = sc1[0][0].split(" ") 
			#print ans
	if len(ans) >= 1:                           # checking for any test list element i.e.  int ,char, void etc with the code of ccextractor
		for k in test:
			if k == ans[0]:
				print sc1[0][0]
	sc1 = []
	ans = []



