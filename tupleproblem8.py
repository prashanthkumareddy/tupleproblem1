from copy import deepcopy
x = ('sonali',4,'asritha',55.6,[23],True)
print(x)

y = deepcopy(x)
y[4].append(46)
print(y)
print(x)
