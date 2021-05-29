# Write your code here :-)
def moonWeight(weight, increase):
    for year in range(1, 16):
        weight = weight + increase
        moonWeight = weight * 0.165
        print('Year %s is %s' % (year, moonWeight))

moonWeight(109, .25)


