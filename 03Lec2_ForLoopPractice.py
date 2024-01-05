import random
import re

##Part A##

#1) Write a for loop that prints 0 to 100


for i in range(0,101):
    if i%2==0:
        print(i)

    
#2) Change the loop such that it only prints even numbers.
##  Use the remainder operator to see if the remainder is 0. If it is
##  0 print the number.
x=2
y=x%2
print(y)
x=3
y=x%2
print(y)


#(1) Writing files: This is the code from the last lecture

fout=open("Temp.txt","w")
output="Statue of Liberty!\n"
fout.write(output)
fout.close()  ### SO ANNOYING 

#(2) What if you forget close the file? The Python solution: use "with"!
# You don't have to remember to close the file when you use with! 

## Here is an example using with. Modify it so that it actually writes
## your name to the file and writes it the number of time = to your birthday!

with open("Temp2.txt", "w") as f:
    output="Anais"
    f.write(output)


#(3) Reading files: Here is some code that reads in the information from a file.
# Let's modify it so that it uses the with so we don't have to use the close method:

"""
fin=open("Temp2.txt","r")
for line in fin:
    print (line)

fin.close()
"""
##Part B##

#1) Open the file named 'junkdata.txt' and print out every line of
#   the file.
#2) Improve it before printing out the data by cleaning up the bad stuff
#   using the string functions and print the good stuff

#3) Open another file called 'gooddata.txt' for reading.
#4) Write the good data to the file with the write function.


##Part C##

#1) Only write to the sequences to gooddata.txt if
#     they start with an ATG
#2) Only write if they start with an ATG and contain the following
#     3 letter sequence motif:
#     GAG
#     TAG
#     TTG
#
###Example of how to use the re (regular expression) module
### to search for a match in a string
dna='AGA'
if re.search('[GT]A',dna):
    print("found it!")
