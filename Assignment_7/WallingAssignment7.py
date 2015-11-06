probability = [0.82, 0.56, 0.08, 0.81, 0.34, 0.22, 0.37, 0.99, 0.55, 0.61, 0.31, 0.66, 0.28, 1.0, 0.95, 0.71, 0.14, 0.1, 1.0, 0.71, 0.1, 0.6, 0.64, 0.73, 0.39, 0.03, 0.99, 1.0, 0.97, 0.54, 0.8, 0.97, 0.07, 0.69, 0.43, 0.29, 0.61, 0.03, 0.13, 0.14, 0.13, 0.4, 0.94, 0.19, 0.6, 0.68, 0.36, 0.67, 0.12, 0.38, 0.42, 0.81, 0.0, 0.2, 0.85, 0.01, 0.55, 0.3, 0.3, 0.11, 0.83, 0.96, 0.41, 0.65, 0.29, 0.4, 0.54, 0.23, 0.74, 0.65, 0.38, 0.41, 0.82, 0.08, 0.39, 0.97, 0.95, 0.01, 0.62, 0.32, 0.56, 0.68, 0.32, 0.27, 0.77, 0.74, 0.79, 0.11, 0.29, 0.69, 0.99, 0.79, 0.21, 0.2, 0.43, 0.81, 0.9, 0.0, 0.91, 0.01]

c = 0.0
rc = 0.0
rnc = 0.0
sc = 0.0
snc = 0.0
wsr = 0.0
wsnr = 0.0
wnsr = 0.0
wnsnr = 0.0
#def setup(lis):
i = 0
#while (i < len(probability)):
#	if (probability[i] < 0.5):	#c
#		c += 1
#	i += 1
#	if (probability[i] < 0.8):	#r|c
#		rc += 1
#	if (probability[i] < 0.2):	#r|~c
#		rnc += 1
#	i += 1
#	if (probability[i] < 0.1):	#s|c
#		sc += 1
#	if (probability[i] < 0.5):	#s|~c
#		snc += 1
#	i += 1
#	if (probability[i] < 0.99):	#w|sr
#		wsr += 1
#	if (probability[i] < 0.9):	#w|s~r
#		wsnr += 1
#	if (probability[i] < 0.9):	#w|~sr
#		wnsr += 1
#	if (probability[i] == 0.0):	#w|~s~r
#		wnsnr += 1
#	i += 1

sb = False
rb = False
while (i < len(probability)):
	if (probability[i] < 0.5):	#c
		c += 1
		if (probability[i + 1] < 0.1):	#s|c
			sc += 1
			sb = True
		if (probability[i + 2] < 0.8):	#r|c
			rc += 1
			rb = True
	else:
		if (probability[i + 1] < 0.5):	#s|~c
			snc += 1
			sb = True
		if (probability[i + 2] < 0.2):	#r|~c
			rnc += 1
			rb = True
	if sb and rb:	
		if (probability[i + 3] < 0.99):	#w|sr
			wsr += 1
	if sb and not rb:
		if (probability[i + 3] < 0.9):	#w|s~r
			wsnr += 1
	if not sb and rb:
		if (probability[i + 3] < 0.9):	#w|~sr
			wnsr += 1
	if not sb and not rb:
		if (probability[i + 3] == 0.0):	#w|~s~r
			wnsnr += 1
	i += 4

def cTrue(lis):
	#count = 0.0
	#i = 0
	#while (i < len(lis)):
	#	if (lis[i] < 0.5):
	#		count +=1
	#		print "hello"
	#	i += 4
	#count = count/25		
	return c/25

def cTrueGivenRTrue(lis):
	#num = 0.0
	#denom = 0.0
	#i = 0
	#size = len(lis)
	#while (i < size):
	#	if (lis[i] < .5):
			#Cloudy
	#		i += 2
	#		if (lis[i] < .8):
	#			#rc
	#			num += 1
	#			denom += 1
	#	else:
	#		i += 2
	#		if (lis[i] >= .8):
	#				denom += 1	
	#	i += 2		 			
	#return num/denom
	return rc/(rc+rnc)

def sGivenWTrue(lis):
	swtrue = wsr + wsnr
	wtrue = wsr + wsnr + wnsr + wnsnr
	return swtrue / wtrue

print cTrue(probability)
print cTrueGivenRTrue(probability)
print sGivenWTrue(probability)
