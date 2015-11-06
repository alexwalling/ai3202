probability = [0.82, 0.56, 0.08, 0.81, 0.34, 0.22, 0.37, 0.99, 0.55, 0.61, 0.31, 0.66, 0.28, 1.0, 0.95, 0.71, 0.14, 0.1, 1.0, 0.71, 0.1, 0.6, 0.64, 0.73, 0.39, 0.03, 0.99, 1.0, 0.97, 0.54, 0.8, 0.97, 0.07, 0.69, 0.43, 0.29, 0.61, 0.03, 0.13, 0.14, 0.13, 0.4, 0.94, 0.19, 0.6, 0.68, 0.36, 0.67, 0.12, 0.38, 0.42, 0.81, 0.0, 0.2, 0.85, 0.01, 0.55, 0.3, 0.3, 0.11, 0.83, 0.96, 0.41, 0.65, 0.29, 0.4, 0.54, 0.23, 0.74, 0.65, 0.38, 0.41, 0.82, 0.08, 0.39, 0.97, 0.95, 0.01, 0.62, 0.32, 0.56, 0.68, 0.32, 0.27, 0.77, 0.74, 0.79, 0.11, 0.29, 0.69, 0.99, 0.79, 0.21, 0.2, 0.43, 0.81, 0.9, 0.0, 0.91, 0.01]

c = 0.0
R = 0.0
cR = 0.0
W = 0.0
sW = 0.0
sCW = 0.0
CW = 0.0


i = 0
while (i < len(probability)):
	if (probability[i] < .5):								#cloudy
		c += 1
		if (probability[i + 1] < .1):							#Sprinkler|cloudy = true
			if (probability[i + 2] < .8):						#rain|cloudy = true
				R += 1
				cR += 1
				if (probability[i + 3] < .99):					#wet grass|sprinkler = true & rain = true
					W += 1
					sW += 1
					CW += 1
					sCW += 1
			else:
				if (probability[i + 3] < .90):
					W += 1
					sW += 1
					CW += 1
					sCW += 1
		else:
			if (probability[i + 2] <.8):
				R += 1
				cR += 1
				if (probability[i + 3] < .90):
					W += 1
					CW +=1	
	else:													#not cloudy
		if (probability[i + 1] < .5):
			if (probability[i + 2] < .2):
				if (probability[i + 3] < .99):
					W += 1
					sW += 1
			else:
				if (probability[i + 3] < .90):
					W += 1
					sW += 1
			if (probability[i + 2] >= .8):
				R += 1
		else:
			if (probability[i + 2] < .2):
				if (probability[i + 3] < .90):
					W +=1
			if (probability[i + 2] >= .8):
				R += 1
	i += 4


def cTrue():
	return c/25

def cTrueGivenRTrue():
	return cR/R

def sGivenWTrue():
	return sW / W
def sGivenCTrueWTrue():
	return sCW / CW
def cReject():
	c = 0.0
	for i in probability:
		if (i < .5):
			c += 1
	return c/len(probability)
def cGivenRTrueReject():
	i = 0
	sample = []
	while i < len(probability):
		if probability[i] < .5:
			if probability[i+1] < .8:
				sample.append(probability[i])
				sample.append(probability[i+1])
		else:
			if probability[i+1] < .2:
				sample.append(probability[i])
				sample.append(probability[i+1])
		i += 2
	i = 0
	cR = 0.0
	R = 0.0
	while i < len(sample):
		if sample[i] < .5:
			i += 1
			if sample[i] < .8:
				cR += 1
				R += 1
				i += 1
		else:
			i += 1
			if sample[i] < .2:
				R += 1
			i += 1
	return cR/R

def sGivenWTrueReject():
	i = 0
	sample = []
	while (i < len(probability)):
		if (probability[i] < .5):
			i += 1
			if (probability[i] <.1):
				i += 1
				if (probability[i] < .8):
					i +=1
					if (probability[i] < .99):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
				else:
					i += 1
					if (probability[i] < .90):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
			else:
				i +=1
				if (probability[i] < .8):
					i += 1
					if (probability[i] < .9):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
				else:
					i += 2			
		else:
			i += 1
			if (probability[i] < .5):
				i += 1
				if (probability[i] < .2):
					i += 1
					if (probability[i] < .99):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
				else:
					i += 1
					if (probability[i] < .9):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
			else:
				i += 1
				if (probability[i] < .2):
					i += 1
					if (probability[i] < .99):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
				else:
					i += 2	
	i = 0
	sW = 0.0
	while (i < len(sample)):
		if (sample[i] < .5):
			i += 1
			if (sample[i] < .1):
				sW += 1
		else:
			i += 1
			if (sample[i] < .5):
				sW += 1
				
		i += 3				
					
	return sW / (len(sample)/4)	

def sGivenCTrueWTrue():
	i = 0
	sample = []
	while (i < len(probability)):
		if (probability[i] < .5):
			i += 1
			if (probability[i] <.1):
				i += 1
				if (probability[i] < .8):
					i +=1
					if (probability[i] < .99):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
				else:
					i += 1
					if (probability[i] < .90):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
			else:
				i +=1
				if (probability[i] < .8):
					i += 1
					if (probability[i] < .9):
						sample.append(probability[i-3])
						sample.append(probability[i-2])
						sample.append(probability[i-1])
						sample.append(probability[i])
					i += 1	
				else:
					i += 2	
		else: i += 3					
	sCW = 0.0		
	i = 0
	while (i < len(sample)):
		if (sample[i] < .5):
			i += 1
			if (sample[i] < .1):
				sCW += 1		
		i += 3				
	return sCW / (len(sample)/4)	



print ("1a) %.2f" % cTrue())
print ("1b) %.2f" % cTrueGivenRTrue())
print ("1c) %.2f" % sGivenWTrue())
print ("1d) %.2f" % sGivenCTrueWTrue())
print ('-------------------------------------')
print ("3a) %.2f" % cReject())
print ("3b) %.12f" % cGivenRTrueReject())
print ("3c) %.2f" % sGivenWTrueReject())
print ("3d) %.2f" % sGivenCTrueWTrue())
