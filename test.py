#
#Integ of Random
#Copyright James Robinson 2018
#All rights reserved
#

from random import randint
import sys

def randomNum():
	return(randint(0,9))

i = 0
results = {0:0, 1:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
numOfTimes = int(sys.argv[1])
num = 0

while i <= numOfTimes:

    num = randomNum()
    results[num] += 1
    i += 1

print("\n", f"The results are:\n{results}\n")


    