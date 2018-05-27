#from sys import argv
from os.path import exists

#script, from_file, to_file = argv
print("Are there files you need to copy in this directory")
print("Press enter for yes or CTRL-C to stop the script.")
input()

#Asks the user for the file to copy. Then asks for the file to copy to.
#If the file does not exist it will create it and populate it.
print("Specify the file to extract from:")
from_file = input()

print("Specify the file to Copy to:")
to_file = input()

print(f"Copying from{from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file).read()

# Lets you know if the file exists and prompts to start the copy.
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Takes the data from the first file and copies to the new file.
out_file = open(to_file, 'w').write(in_file)

print("Alright, all done.")
