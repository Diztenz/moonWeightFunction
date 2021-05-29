# Write your code here :-)
import sys

def moonWeight():
    print('Please enter your current Earth weight')
    weight = float(sys.stdin.readline()) #float standard input
    print('Please enter the amount your weight might increase each year')
    increase = float(sys.stdin.readline()) #float standard input
    print('Please enter the number of years')
    years = int(sys.stdin.readline())
    years = years + 1 #because last number in range does not get added
    for year in range(1, years): # last number in range does not get added.
        weight = weight + increase
        moonWeight = weight * 0.165
        print('Year %s is %s' % (year, moonWeight))




