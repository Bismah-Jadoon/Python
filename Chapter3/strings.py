# String 

# a = "hello" #type is string
# b = "23" # type is string

# print(type(a), type(b))

               ###############################################################

#  String Slicing
# name = "Shine"
# slice = name[0:3] # start from 0 index and end at (length-1) 2
# print(slice) 
      
              #################################################################

# indexing
# name = "Shine"
# slice = name[1:] # start at 1 and end at length which is 4
# slic = name[1:5] #print same as name[1:]

# slice = name[:3] #start at 0 and end at 2 (length-1)

# slice = name[-4: -1] #negative index means the index start from backward

# print (slice)

                ################################################################
 
# SLicing with skip value

name = "Shine"
# skip = name [1 : 5 : 3] # [start_index, end_index, steps] 
# skip = name[:5:2] #[0: 5: 2]
skip = name[0::2] #[0:5:2]
print(skip)

