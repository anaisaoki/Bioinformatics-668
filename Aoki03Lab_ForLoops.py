#-------------------------------------------------------------------------------
#PYTHON LAB 3
#-------------------------------------------------------------------------------


import random
out=open('Aoki03Lab.txt','w')

print("\n########## PART 1 ##########\n")
out.write("\n########## PART 1 ##########\n")

#PART 1 - STRING LOOPING & COUNTING

#(1) Use a "for" loop to iterate through the DNA sequence.
#(2) Count the number of G's and C's in the DNA sequence.
#(3) Print the number of G's and C's in the DNA sequence.

#DATASET FOR PART 1: try each of thes options

#== PART 1 ==

test_dna="GACCTTTAC"
print(test_dna)
out.write(test_dna)
count=0
for i in test_dna:
    if i=='G' or i=='C':
        count+=1
print("Number of G's & C's in the DNA Sequence above is:",count)
out1=str(count)
out.write("Number of G's & C's in the DNA Sequence above is:")
out.write(out1)
    
test_dna="GATCCTGGCTCAGGACGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAGCGGTAAGGCCCTTCGGGGTACACGAGCGGCGAACGGGTGAGTAACACGTGGGTGATCTGGGGCCCCATCTA"
print(test_dna)
out.write(test_dna)

count=0
for i in test_dna:
    if i=='G' or i=='C':
        count+=1
print("Number of G's & C's in this DNA Sequence above is:",count)
out.write("Number of G's & C's in this DNA Sequence above is:")
out12=str(count)
out.write(out12)


#-------------------------------------------------------------------------------
print("\n########## PART 2 ##########\n")
out.write("\n########## PART 2 ##########\n")


#PART 2 - CLEAN the Sequence first then calculate the percentage of G and C

# (1) Clean the DNA sequence.
# (2) Use a "for" loop to iterate through the DNA sequence.
# (3) Count the number of G's and C's in the DNA sequence.
# (4) Calculate the proportion of G and C nucleotides in the DNA sequence.
#       For example this proportion in DNA sequence "GACT" is 0.5. 
# (5) Print the percentage of G and C in the DNA sequence.

#To get percentage divide the count of G and C by the total length of the DNA
#Then multiply by 100. 0.5 becomes 50.0
#For example: len(clean_dna)


#== PART 2 ==

nasty_dna="\n AgGctgTtgC \t\n".upper().strip()
print(nasty_dna)
out.write(nasty_dna)

gc_count=0
for base in nasty_dna:
    if base=='G' or base=='C':
        gc_count+=1
print("Number of C's & G's in this sequence is:", gc_count)
out2=str(gc_count)
out.write("Number of C's & G's in this sequence is:")
out.write(out2)

base_total=len(nasty_dna)
out3=str(base_total)
print(base_total)
out.write(out3)


proportion_gc=gc_count/base_total
print(proportion_gc)
out4=str(proportion_gc)
out.write(out4)

percentage_gc=proportion_gc*100
print(percentage_gc)
out5=str(percentage_gc)
out.write(out5)

#-------------------------------------------------------------------------------
print("\n########## PART 3 ##########\n")
out.write("\n########## PART 3 ##########\n")


#PART 3 - CHARACTER CLASSIFICATION

dna="AAGGTTCCCCG"*10

# (1) Count the number of each type of base in the DNA sequence.
# (2) Return the counts of each type of base in the DNA sequence.
# (3) Also print out a table of the counts as shown below.

#== PART 3 ==

countA=0
countG=0
countC=0
countT=0
for bases in dna:
    if bases=='A':
        countA+=1
    if bases=='G':
        countG+=1
    if bases=='C':
        countC+=1
    if bases=='T':
        countT+=1
print("Total counts of each base")
out.write("Total counts of each base")
print("    A:   ", countA)
out6=str(countA)
out.write("    A:   ")
out.write(out6)
print("    T:   ", countT)
out7=str(countT)
out.write("    T:   ")
out.write(out7)
print("    G:   ", countG)
out8=str(countG)
out.write("    G:   ")
out.write(out8)
print("    C:   ", countC)
out9=str(countC)
out.write("    C:   ")
out.write(out9)


#The table should look like this:
#   A   9
#   T	10 
#   G	12
#   C	7

#-------------------------------------------------------------------------------
print("\n########## PART 4 ##########\n")
out.write("\n########## PART 4 ##########\n")


#PART 4 - Using range and random


#Use the random.shuffle function to make and print 10 random lists of names.

#names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
#print(names) #prints the unshuffled names

#== PART 4 ==


names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
print("OG LIST:",names)

for i in range(0,10):
    random.shuffle(names)
    print(names)
    out10=str(names)
    out.write(out10)

#-------------------------------------------------------------------------------
print("\n########## PART 5 ##########\n")
out.write("\n########## PART 5 ##########\n")
out.close()

#PART 5 - Write everthing to a file!!

"""
For this last part, write all your results to a file called: YourName03Lab.txt
YourName should be changed to your name of course.

How to do this? It's easy!
(1) Put this code at the top of the file:
outfile=open('YourName03Lab.txt','w')

(2) After each print statement, add a line to write data to a file:

print(names)
out=str(names) # You can only write strings to a file!
outfile.write(out)

(3) At the end of this file put this:

outfile.close()

"""


