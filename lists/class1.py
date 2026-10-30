roll_no=[9,55,1,2,3,4,5,54,55]#valid #integer lists
names=["mani","deepak","naveen"]#valid string lists
mix_list=[1, "jenny","tony", 10.10] # mix also valid
# lists are mutable means after creating  you can change any value
# it is ordered a collection of elements.
# index always start with 0
# using index we can access the elements  of particular item from the lists
# using lists name name also you can access lists of elements.
#In lists duplicates are allowed
print(roll_no)
print(names)
print(mix_list)

#using index we are accessing the lists.
print(roll_no[1])


#length
print(len(roll_no))
print(len(names))
print(len(mix_list))

#slicing
print(roll_no[0:4:2])#[START:STOP:step]
print(roll_no[0:4])
print(roll_no[5::-1])

# sort method
# sorting  of mix_list thrown an error.
roll_no.sort()
print(roll_no)
roll_no.reverse()
print(roll_no)

# first short and then print otherwise you will get answer NONE
#min and max
print(min(roll_no))
print(max(roll_no))

# while using append function one  argument will pass at a  time.
roll_no.append(66)
print(roll_no)

# while using  insert function  multiple arguments  at a time
roll_no.insert(1,89)
print(roll_no)

#Extend_function
roll_no.extend([11,22,33,44])
print(roll_no)







