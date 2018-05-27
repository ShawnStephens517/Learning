
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you are {age} old, {height} tall and {weight} heavy.")

print("What is the number?", end= ' ')
x = int(input())
print("Do some adding", end= ' ')
y = int(input())

#Working on taking specific basic math operators and doing something with x,y
print("What do you want to do with these numbers?", end=' ')
operator = input()

print(f"So, your favorite number is:", int(x) + int(operator) + int(y))
