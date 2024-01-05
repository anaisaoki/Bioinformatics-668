########Reading and Writing Files#######

#(1) Writing files
#What does this do?

fout=open("Temp.txt","w")
output="Statue of Liberty!\n"
fout.write(output)
fout.close()

#Modify the above code so that it writes "I love the:" and then
#"Statue of Liberty!" 153 times, each time on a different line.

## Where is your FILE on the computer??

#(2) Reading files
# Modify the following code to read in a file called "03ALprimate.nex"
# You should be able to find it in course documents.

"""
fin=open("Temp.txt","r")

for line in fin:
    print (line)

fin.close()  #ALWAYS close your files when you are done with them.

"""



