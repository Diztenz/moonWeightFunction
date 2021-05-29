# Write your code here :-)
def moonWeight(weight, increase, years):
    for year in range(1, years): # 25 years is actually from 1-26 last number in range does not get added.
        weight = weight + increase
        moonWeight = weight * 0.165
        print('Year %s is %s' % (year, moonWeight))




