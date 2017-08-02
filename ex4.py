#how many cars
cars = 100
#how much space in a car
space_in_a_car = 4.0
#how many drinvers can drive the car
drivers = 30
#how many passengers may drive the car
passengers = 90
#how many cars can't be driven
cars_not_driven = cars-drivers
#how many cars can be driven
cars_driven = drivers
#how much space in all cars
carpool_capacity = cars_driven*space_in_a_car
#how many passengers in each cars
average_passengers_per_car = passengers/cars_driven


print "There are",cars,"cars  available"
print "There are only",drivers,"drivers available."
print"There will be",cars_not_driven,"empty cars today."
print "we can transport",carpool_capacity,"people today"
print"We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
