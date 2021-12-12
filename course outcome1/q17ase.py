import operator

d={"a":6,"c":9,"b":2,"e":1,"f":0}

s= sorted(d.items(), key=operator.itemgetter(1))

print('ascending order : ',s)

s1= dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print('descending order : ',s1)