##
#  
#  Plans drone delivery trips from a warehouse to a customer and reports
#  the straight-line distance, number of trips, total distance flown,
#  and total time (flying + loading).
#
#  PART A - HAND CALCULATION  (3 km east, 4 km north, 40 km/h, 7 packages, 2 per trip)
#
#  Import style: "import math" - writing math.sqrt and math.ceil makes it
#  clear to any reader which module each function comes from.
#
import math

packages = 7
packages_per_trip = 2

straightLineDistance = math.sqrt((3 ** 2) + (4 ** 2)) # Should be 5
print("Straight line distance:", straightLineDistance)

totalTrips = (packages // packages_per_trip) + (packages % packages_per_trip) # Should be 4
print("Total number of trips:", totalTrips)

distanceFlown = straightLineDistance * totalTrips
print("Total distance flown:", distanceFlown, "km")

timeFlying = distanceFlown / 40 # 40 is the km per hour

print("The total time flown is:", timeFlying, "hours")


