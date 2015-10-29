#Bayes Network
```
python WallingAssignment6.py -<args>
```

##Marginal examples
```
python cli.py -mD 
		---0.304
python cli.py -mS 
		---0.3
python cli.py -mC 
		---0.011
```
##Conditional examples
```
python cli.py -g"C|S" 
		---0.032
python cli.py -g"d|S" 
		---0.311
python cli.py -g"C|C" 
		---1
```
##Joint examples
```
python cli.py -jPSC 
		---P(P,S,C) 0.0081
		---P(P,S,~C) 0.00063
		---P(~P,~S,C) 0.0015
		---P(~P,~S,C) 0.0014
		---P(P,S,~C) 0.2619
		---P(P,~S,~C) 0.62937
		---P(~P,S,~C) 0.0285
		---P(~P,~S,~C) 0.0686
python cli.py -jpsc
		---P(P,S,C) 0.0081
python cli.py -j~p~s~c
		---P(~P,~S,~C) 0.0686
```
