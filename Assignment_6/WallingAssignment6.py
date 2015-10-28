import getopt
import sys

class Node():
	def init(self):
		self.parents = []
		self.conditionals = {}

	def setParents(self, p):
		for i in p:
			self.parents.append(i)

	def setConditionals(self, c, p):
		self.conditionals[c] = p

	def getParent(self):
		return self.parents

	def getConditionals(self):
		return self.conditionals
	

def marginal(graph, args):
	if args is "P":
		return graph["Pollution"].getConditional()["p"]
	elif args is "S":
		return graph["Smoker"].getConditional()["s"]
	elif args is "C":
		condition = graph["Cancer"].getConditional()
		polution = graph["Pollution"].getConditional()["p"]
		smoker = graph["Smoker"].getConditional()["s"]
		
		p = (condition["ps"]*smoker) + (condition["p~s"]*(1-smoker))

		notp = (condition["~ps"]*smoker)+ (condition["~p~s"]*(1-smoker))
		return (pollution*p) + ((1-pollution)*notp)
	elif args is "X":
		condition = graph["XRay"].getConditional()
		cancer = marginal(graph, "C")[1]
		return (condition["c"]*cancer) + (condition["~c"]*(1-cancer))
	elif args is "D":
		condition = graph["Dyspnoea"].getConditional()
		cancer = marginal(graph, "C")[1]
		return (condition["c"]*cancer) + (condition["~c"]*(1-cancer))

def conditional():
	pass
def joint():
	pass

if __name__ == "__main__":
	network = {}
	
	network["Pollution"] = Node()
	network["Smoker"] = Node()
	network["Cancer"] = Node()
	network["XRay"] = Node()
	network["Dyspnoea"] = Node()
	
	network["Cancer"].set_parents([network["Pollution"],network["Smoker"]])
	network["XRay"].set_parents([network["Cancer"]])
	network["Dyspnoea"].set_parents([network["Cancer"]])
	
	network["Pollution"].set_conditional("p",0.9)
	
	network["Smoker"].set_conditional("s",0.3)
	
	network["Cancer"].set_conditional("~ps",0.05)
	network["Cancer"].set_conditional("~p~s",0.02)
	network["Cancer"].set_conditional("ps",0.03)
	network["Cancer"].set_conditional("p~s",0.001)
	
	network["Cancer"].set_conditional("s~p",0.05)
	network["Cancer"].set_conditional("~s~p",0.02)
	network["Cancer"].set_conditional("sp",0.03)
	network["Cancer"].set_conditional("~sp",0.001)
	
	network["XRay"].set_conditional("c",0.9)
	network["XRay"].set_conditional("~c",0.2)
	
	network["Dyspnoea"].set_conditional("c",0.65)
	network["Dyspnoea"].set_conditional("~c",0.3)
