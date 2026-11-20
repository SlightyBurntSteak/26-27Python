##
#  Section 11.7 Worked Example: Computing Travel Time
#  A robot drives along a road (fast), then cuts straight across rocky
#  terrain (slow) to reach an item. Compute the total travel time.
#
#  HAND CALCULATION (r1 = 10 km, dy = 3 km, l1 = 6 km, s1 = 5 km/h, s2 = 2 km/h):
#    Segment 1 time   = 6 / 5 = 1.2
#    Segment 2 length = 5.0
#    Segment 2 time   = 2 / 5 = 0.4
#    Total time       = 1.6 hours
#
from math import sqrt

# Short hand-calculation names (dx, s1...) become DESCRIPTIVE names in code.

# Segment 1

length1 = input("Enter the length of Segment 1: ")
speed1 = input("Enter how fast you are going in Segment 1 (in km): ")
length1 = int(length1)
speed1 = int(speed1)
time1 = length1 / speed1
print("The time it took for Segment 1 is: ", time1)



## Segment 2

distanceX = input("Enter distance x: ")
distanceY = input("Enter distance y: ")
speed2 = input("Enter how fast you are going in Segment 2 (in km): ")
### Converts the strings into intigers 
distanceX = int(distanceX)
distanceY = int(distanceY)
speed2 = int(speed2)
length2 = sqrt((distanceX ** 2) + (distanceY ** 2))
print("The length of Segment 2 is", length2, "km")
time2 = length2 / speed2
print("The time it took for Segment 2 is: ", time2)
timeTotal = time1 + time2
print("The total time is: ", timeTotal)






# ---------------------------------------------------------------
# TRY IT
#  1. Run with 10, 3, 6, 5, 2.  Does the program match the hand value 3.7?
#  2. By hand: what if the robot drives 8 km on the road instead of 6?
#     (Hint: segment 2 becomes a 2-3 right triangle.) Then check it.
#  3. Rewrite the import as "import math". What else must change?
# ---------------------------------------------------------------
