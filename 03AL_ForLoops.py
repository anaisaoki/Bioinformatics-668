
####### Using For loops #######
# For loops are the "smart" loops.
# They know: (1) How to move and (2) When to stop.

print("\n### Part A ###")
####### Part A: For loop with strings  #######
# Here is a for loop that is doing what len() does.
# (1) Fix the error.
# (2) Test the loop and fix if necessary.

"""Iterates through a string and returns its length"""
data="   AGACGTTCTAC\n".strip()
count=0
data=data.strip()
print(data)
#set counter to zero BEFORE the loop (why not inside the loop?)
#FIX the LOOP
new_dna="AGACGTTCTAC"
count=0
for i in data:  #How does this work? What is i? print(i) to find out!
    count+=1#Add a statement to print i each time
    print(count)


# Is the length what you expected? How could you make it better?
#     (Hint: try cleaning up data before the for loop.)
# What would you have to change in the loop above to make it
#     work with a new variable: new_dna="AGAGTCCT" ?

print("\n### Part B ###")
####### Part B: For loop with list data #######
# Below is a list of students. What is the for loop doing?
# Modify the for loop so that it counts the number of "Bob"s and then
# prints this value.

bio_class=['Bob','Jo','Bob','Martin','Eve','DJ Spooky','Bob']
for student in bio_class:
    if student=="Bob":
        bobs+=1
    print(student)



print("\n### Part C ###")
####### Part C: For loop with the range function #######
# Figure out what looping through these range functions is doing.
# (1) Explain how each is working in a comment.
# (2) Use the for loop to break up a string (below).

for i in range(5):
    print(i)

#change to range(3,10)
#change to range(0,100,5)

