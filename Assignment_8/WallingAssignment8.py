import sys

#help from Dawson Botsford
#comment out sys.stdout = open("output.txt", "w") if you want command line output
sys.stdout = open("output.txt", "w")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']

def marginal(file):
	count = {}
	for letter in letters:
		count[letter] = 0
	
	f = open(file, 'r')
	for line in f:
		count[line[0]] += 1

	sum = 0

	for key, value in count.iteritems():
		prob = float(value) / 160980
		sum += prob
		print 'P(%s) = %.5f ' %(key, prob)

def stateSum(fileName, character):
	f = open(fileName, 'r')
	sum = 0
	for line in f:
		if (line[0] == character):
			sum += 1
	return sum


def emission(file):
	count = {}
	for letter in letters:
		evidence = {}
		for letter2 in letters:
			evidence[letter2] = 1  #smoothing
		count[letter] = evidence

	f = open(file, 'r')
	for line in f:
		count[line[0]][line[2]] += 1

	for stateKey, stateValue in count.iteritems():
		sumOfState = 0
		for evidenceKey, evidenceValue in stateValue.iteritems():
			prob = float(float(evidenceValue) / float((27 + stateSum(file, stateKey))))
			sumOfState += prob
			print 'P(%s|%s) = %.5f ' %(evidenceKey, stateKey, prob)

def transition(file):
	count = {}
	for letter in letters:
		evidence = {}
		for letter2 in letters:
			evidence[letter2] = 1 #smoothing
		count[letter] = evidence

	f = open(file, 'r')

	curr = f.readline()
	for line in f:
		count[curr[0]][line[0]] += 1
		curr = line

	for stateKey, stateValue in count.iteritems():
		sumOfState = 0
		for evidenceKey, evidenceValue in stateValue.iteritems():
			prob = float(float(evidenceValue) / float((27 + stateSum(file, stateKey))))
			sumOfState += prob
			print 'P(%s|%s)  = %.5f' %(evidenceKey, stateKey, prob)


marginal('typos20.data')
emission('typos20.data')
transition('typos20.data')
