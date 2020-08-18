# After the exercise. I will find my annual salary using variablesself.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers /cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print ("we can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


#Here is the salary for now and potential in 10 years based on 2% increases
#annually

paycheck = 2291.84
taxes = paycheck * .25
salary = (paycheck+taxes) *26
increase = salary *.03
newsal = (increase+salary)
two_bonus = (newsal *.03)
two_year = two_bonus+ newsal
print (salary)
print (two_year)
