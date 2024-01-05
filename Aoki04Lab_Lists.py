
#----------------------------------------------------------------------------
#PYTHON LAB 4: LISTS
#----------------------------------------------------------------------------

import random
outfile=open('Aoki04Lab.txt','w')

print("\n########## PART 1 ##########\n")

#PART 1 - Append substrings to a list

#(1) Use a or loop to iterate through a sequence.
#(2) Divide the sequence into sections of 3 DNA bases with NO OVERLAP.
#(3) Append the 3-base codons to a list.
#[NOTE: If a group is not 3 bases long, do not include it in the list.]
#(4) Print the final list. 

#== PART 1 ==

#for sequence 1
print("For Sequence 1")
seq1="AUGGGAAGC"   #This should print  ["AUG","GGA","AGC"]
list=[]
for i in range(0,len(seq1),3):
    codon1=seq1[i:i+3]
    if len(codon1)==3:
        list.append(codon1)
print(list)

    
#for sequence 2
print("For Sequence 2")
seq2="AUGGGAAGCGGCG"#This should print  ["AUG","GGA","AGC","GCG"]
list=[]
for i in range(0,len(seq2),3):
    codon2=seq2[i:i+3]
    if len(codon2)==3:
        list.append(codon2)
print(list)



#Here is a little snippet of code that should help.
#It uses a for loop to 'break up' a string into groups of 3 characters
# like with codons. Question - how do you then append then to a list?



#-------------------------------------------------------------------------------
print("\n########## PART 2 ##########\n")

#PART 2 - Change the length of the substrings

# Exactly the same as part 1 EXCEPT instead of 3-characters
#    it can be of length x, where x is an integer.
# For example if x=4, then if seq='AAAAGGGGCCCC' the loop would print
# ['AAAA','GGGG','CCCC']
# Feel free to copy past and modify the loop from part 1

#== PART 2 ==

#Try it out with two different values of x and two different sequences



#for sequence 1
print("For Sequence 1")
seq1="AAAAGGGGCCCC"
x=4
list=[]
for i in range(0,len(seq1),x):
    codon1=seq1[i:i+x]
    if len(codon1)==x:
        list.append(codon1)
print(list)

#forsequence 2
print("For Sequence 2")
seq2="AUGUAUGUCUGUCUGAUC"
x=5
list=[]
for i in range(0,len(seq2),x):
    codon2=seq2[i:i+x]
    if len(codon2)==x:
        list.append(codon2)
print(list)


#------------------------------------------------------------------------------
print("\n########## PART 3 ##########\n")
#PART 3 -  Iterate through a list of strings, calculate value, write to file


#(1) Iterate through the list of sequences
#(2) Count G's and C's for each sequence nmer in a list.
#(3) Calculate the GC Percentage for the sequence nmer.
#(4) Write the sequence and its GC percentage (separated by a "Tab")
#    to a file named:
#       gc_output.txt

###A counting shortcut for string data:
seq="AGGT"
g_count=seq.count("G")
print(g_count)

#For example if given the following sequence list
#seq_list=["AAUG","AGCG","GCUA"]

#The loop would write the following to the file gc_output.txt
#AAUG    25.0
#AGCG    75.0
#GCUA    50.0

#== PART 3 ==

seq_list=["AAUG","AGCG","GCUA"]
#seq_list=["AAUGGAGACU","AGCGCCCC","GCUAAAAAAU"]

for seq in seq_list:
   x==len(seq)
   gc_count=seq.count("G")+seq.count("C")
   a=(gc_count/x)*100
   print(seq)
   out=str(seq)
   outfile.write(out)
   print(a)
   out=str(a)
   outfile.write(out)

outfile.close()




