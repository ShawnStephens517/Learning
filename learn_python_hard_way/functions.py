def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have{cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give numbers directly:")
cheese_and_crackers(20, 40)

print("How many cheese squares do you have?")
amount_of_cheese = input()
print("How many cracker do you have?")
amount_of_crackers = input()

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(int(amount_of_cheese) + 100,
                    int(amount_of_crackers) + 10000)
