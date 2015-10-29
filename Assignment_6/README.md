#Bayes Network
```
python WallingAssignment6.py <args>
```

##Marginal examples
```
python cli.py -mD --- 0.304
python cli.py -mS --- 0.3
python cli.py -mC --- 0.011
```
##Conditional examples
```
python cli.py -g"C|S" --- 0.032
python cli.py -g"d|S" --- 0.311
python cli.py -g"C|C" --- 1
```
##Joint examples
```
python cli.py -jPSC 
python cli.py -jpsc
python cli.py -j~p~s~c
```
