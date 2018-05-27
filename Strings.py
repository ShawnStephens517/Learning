# Sets the variables of several items. Types, x, binary, do_not, and y.
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# Sets variable hilarious and joke evaluation. When printed, format
# the joke_evaluation and give the argument of hilarious

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
# Sets the w and e variables and cancatinates the two when printed.
w = " This is the left side of..."
e = " a string with a right side."

print(w + e)
