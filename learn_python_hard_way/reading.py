from sys import argv
#Input a command line argument of the file that should be printed later
script, filename = argv
txt = open(filename)
#Prints the file name from the argument entered
print(f"Here's your file {filename}:")
print(txt.read())

#Asks to put in the file name again. You could also read another filename here.
print("Type the filename again:")
file_again = input("☼ ")

txt_again = open(file_again)

print(txt_again.read())
