import getopt
import sys

class Node():
	def __init__(self):
		self.parents = []
		self.conditionals = {}

	def setParents(self, p):
		for i in p:
			self.parents.append(i)

	def setConditionals(self, c, p):
		self.conditionals[c] = p

	def getParent(self):
		return self.parents

	def getConditional(self):
		return self.conditionals
	

def marginal(graph, args):
	if args is "P":
		return graph["Pollution"].getConditional()["p"]
	elif args is "S":
		return graph["Smoker"].getConditional()["s"]
	elif args is "C":
		condition = graph["Cancer"].getConditional()
		pollution = graph["Pollution"].getConditional()["p"]
		smoker = graph["Smoker"].getConditional()["s"]
		
		p = (condition["ps"]*smoker) + (condition["p~s"]*(1-smoker))

		notp = (condition["~ps"]*smoker)+ (condition["~p~s"]*(1-smoker))
		return (pollution*p) + ((1-pollution)*notp)
	elif args is "X":
		condition = graph["XRay"].getConditional()
		cancer = marginal(graph, "C")#[1]
		return (condition["c"]*cancer) + (condition["~c"]*(1-cancer))
	elif args is "D":
		condition = graph["Dyspnoea"].getConditional()
		cancer = marginal(graph, "C")#[1]
		return (condition["c"]*cancer) + (condition["~c"]*(1-cancer))

def conditional(graph, x, y):
	print "Calculating conditional probability of {0} given {1}".format(x, y)
	if x is y:
		return 1
	else:#TODO
		graph[y].setConditional(y, 1)
		return calc_marginal(graph, x)

	return None	

def parseJoint(args):
	parsed = []
	arg_len = len(args)
	next_has_tilde = False
	for i in range(0,arg_len):
		if args[i] is "~":
			next_has_tilde = True
		else:
			if next_has_tilde:
				parsed.append("~"+args[i])
				next_has_tilde = False
			else:
				parsed.append(args[i])
	return parsed

def joint(graph, args):
	pollution = graph["Pollution"].getConditional()
	smoker = graph["Smoker"].getConditional()
	cancer = graph["Cancer"].getConditional()

	if "P" in args and "S" in args and "C" in args:
		print "P(P,S,C) " + str(cancer["ps"] * pollution["p"] * smoker["s"])
		print "P(P,S,~C) " + str(cancer["p~s"] * pollution["p"] * (1 - smoker["s"]))
		print "P(~P,~S,C) " + str(cancer["~ps"] * (1 - pollution["p"]) * smoker["s"])
		print "P(~P,~S,C) " + str(cancer["~p~s"] * (1 - pollution["p"]) * (1 - smoker["s"]))

		print "P(P,S,~C) " + str((1-cancer["ps"]) * pollution["p"] * smoker["s"])
		print "P(P,~S,~C) " + str((1-cancer["p~s"]) * pollution["p"] * (1 - smoker["s"]))
		print "P(~P,S,~C) " + str((1-cancer["~ps"]) * (1 - pollution["p"]) * smoker["s"])
		print "P(~P,~S,~C) " + str((1-cancer["~p~s"]) * (1 - pollution["p"]) * (1 - smoker["s"]))

	elif "p" in args and "s" in args and "c" in args:
		print "P(P,S,C) " + str(cancer["ps"] * pollution["p"] * smoker["s"])

	elif "~p" in args and "~s" in args and "~c" in args:
		print "P(~P,~S,~C) " + str((1-cancer["~p~s"]) * (1 - pollution["p"]) * (1 - smoker["s"]))

if __name__ == "__main__":
	network = {}
	
	network["Pollution"] = Node()
	network["Smoker"] = Node()
	network["Cancer"] = Node()
	network["XRay"] = Node()
	network["Dyspnoea"] = Node()
	
	network["Cancer"].setParents([network["Pollution"], network["Smoker"]])
	network["XRay"].setParents([network["Cancer"]])
	network["Dyspnoea"].setParents([network["Cancer"]])
	
	network["Pollution"].setConditionals("p",0.9)
	
	network["Smoker"].setConditionals("s",0.3)
	
	network["Cancer"].setConditionals("~ps",0.05)
	network["Cancer"].setConditionals("~p~s",0.02)
	network["Cancer"].setConditionals("ps",0.03)
	network["Cancer"].setConditionals("p~s",0.001)
	
	network["Cancer"].setConditionals("s~p",0.05)
	network["Cancer"].setConditionals("~s~p",0.02)
	network["Cancer"].setConditionals("sp",0.03)
	network["Cancer"].setConditionals("~sp",0.001)
	
	network["XRay"].setConditionals("c",0.9)
	network["XRay"].setConditionals("~c",0.2)
	
	network["Dyspnoea"].setConditionals("c",0.65)
	network["Dyspnoea"].setConditionals("~c",0.3)


	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		print(str(err))
		sys.exit(2)
	for o, a in opts:
		if o in ("-p"):
			if a[0] == "P":
				network["Pollution"].set_conditional("p",float(a[1:]))
			elif a[0] == "S":
				network["Smoker"].set_conditional("s",float(a[1:]))
		elif o in ("-m"):
			print(marginal(network, a))
		elif o in ("-g"):
			(var, given) = a.split('|')
			conditional(network, var, given)
		elif o in ("-j"):
			parsed = parseJoint(a)
			joint(network, parsed)
		else:
			assert False, "unhandled option"
